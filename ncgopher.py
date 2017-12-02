#!/usr/bin/env python
import socket
import tempfile
import sys, os
import traceback

import locale
locale.setlocale(locale.LC_ALL, '')
code=locale.getpreferredencoding()

import curses
global screen
screen=None
def initCurses():
    global screen
    screen=curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    screen.keypad(1)
    curses.init_pair(1, 5, 0)   # Links are magenta on black, or black on magenta

def killCurses():
    global screen
    curses.echo(); curses.nocbreak(); screen.keypad(0); curses.endwin()

GOPHER_ITEM_TYPES=["+", "g", "I", "T", "h", "i", "s", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pageStack=[]
global currentlySelected, selectedLink
currentlySelected=0
selectedLink=None

def displayGopherMenu(page):
    global selectedLink
    lines=page.split("\r\n")
    links=0
    screen.clear()
    for line in lines:
        if(len(line)<8):
            continue
        ltype=line[0]
        lcontent=line[1:].split("\t")
        if(ltype=="i"):
            try:
                screen.addstr(lcontent[0].encode(code)+"\n")
            except:
                pass
        else:
            color=curses.color_pair(1)
            pfx=" o "
            attr=curses.A_UNDERLINE
            if(links==currentlySelected):
                pfx=">> "
                attr=attr|curses.A_REVERSE
                selectedLink=(ltype, lcontent[1:])
            try:
                screen.addstr(pfx+lcontent[0].encode(code)+"\n", color|attr)
            except:
                pass
            links+=1
    screen.refresh()

def navGopherMenu(page):
    global currentlySelected
    currentlySelected=0
    while True:
        displayGopherMenu(page)
        ch=screen.getch()
        if ch==curses.KEY_UP and currentlySelected>0:
            currentlySelected-=1
        elif ch==curses.KEY_DOWN:
            currentlySelected+=1
        elif ch==curses.KEY_RIGHT:
            return selectedLink
        elif ch==curses.KEY_LEFT:
            if(len(pageStack)>1):
                pageStack.pop()
                return pageStack.pop()
        elif ch==ord("q"):
            return None
        elif ch==ord("g"):
            query=curses.newwin(4, 80, 10, 0)
            query.box()
            query.addstr(1, 1, "Address (query, optionally followed by tab-separated address and port):")
            query.overlay(screen)
            screen.refresh()
            query.refresh()
            curses.echo()
            addy=query.getstr(2, 1)
            curses.noecho()
            del query
            screen.refresh()
            if len(addy)>0:
                parts=addy.split("\t")
                if(len(parts)==1):
                    return (None, (addy, pageStack[-1][1][1], pageStack[-1][1][2]))
                elif (len(parts)==2):
                    return (None, (parts[0], parts[1], 70))
                else:
                    return (None, (parts[0], parts[1], parts[2]))



def fetchGopherObject(addr, host, port):
    s=socket.socket()
    try:
        s.connect((host, int(port)))
    except:
        print("Error: could not connect to host "+host+" on port "+str(port))
        return None
    s.sendall(addr+"\r\n")
    page=[]
    ret=s.recv(4096)
    while(len(ret)>0):
        page.append(ret)
        ret=s.recv(4096)
    s.close()
    return "".join(page)
    
pager=os.getenv("PAGER")
if not pager:
    pager="less"

def guessIfPageIsMenu(page):
    if(not page):
        return False
    if(len(page)==0):
        return False
    line=page.split("\r\n")[0]
    if line[0] in GOPHER_ITEM_TYPES:
        fields=line.split("\t")
        if(len(fields)>=2):
            return True
    return False
def errMsg(msg):
        query=curses.newwin(4, 80, 10, 0)
        query.box()
        query.addstr(1, 1, msg)
        query.addstr(2, 1, "PRESS ANY KEY TO CONTINUE")
        query.overlay(screen)
        screen.refresh()
        query.refresh()
        query.getch()
        del query
        screen.refresh()
def displayGopherObject(addr, host, port, itype=None):
    page=fetchGopherObject(addr, host, port)
    if not page:
        errMsg("Couldn't load page gopher://"+str(host)+":"+str(port)+"/"+str(addr))
        if(len(pageStack)>0):
            return pageStack.pop()
        return None
    if itype==None:
        if(guessIfPageIsMenu(page)):
            itype='1'
        else:
            itype='0'
    if(itype=="1"):
        pageStack.append((itype, (addr, host, port)))
        return navGopherMenu(page)
    else:
        temp=tempfile.NamedTemporaryFile(delete=False)
        temp.write(page)
        temp.flush()
        temp.close()
        killCurses()
        os.system(pager+"<"+temp.name)
        initCurses()
        os.unlink(temp.name)
    if(len(pageStack)>0):
        return pageStack.pop()
    return None

def main():
    if(len(sys.argv)<3):
        print("Usage: "+sys.argv[0]+" query hostname [port]")
        sys.exit(1)
    port=70
    if(len(sys.argv)>=4):
        port=sys.argv[3]
    initCurses()
    try:
        nextItem=(None, (sys.argv[1], sys.argv[2], port))
        while nextItem!=None:
            nextItem=displayGopherObject(nextItem[1][0], nextItem[1][1], nextItem[1][2], nextItem[0])
    except:
        killCurses()
        traceback.print_exc()
    killCurses()

if __name__=="__main__":
    main()
