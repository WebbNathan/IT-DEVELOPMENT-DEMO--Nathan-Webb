'''
Written by Nathan Webb; netid: webbn; Code demo for IT Development job position; March 27th 2024

Code runs a calender application using pygame. The calender allows for the user to navigate to years and months,
and displays the corresponding dates and weekdays. The user can click on a text box at the bottom of the page that
allows for numerical input, which when entered, brings the user to another page that allows for notes to be written,
as one would on a physical calender. What the user types is saved to a json file with dates as keys, and is saved 
to the users computer.

github repository: https://github.com/WebbNathan/IT-DEVELOPMENT-DEMO--Nathan-Webb

'''

import pygame, sys,os, json
from datetime import date, datetime

def daysInCurrentMonth(dateObj):
    if(dateObj.month != 12):
        daysInMonth = date(dateObj.year, dateObj.month + 1, 1) - date(dateObj.year, dateObj.month, 1)
    else:
        daysInMonth = date(dateObj.year + 1, 1, 1) - date(dateObj.year, dateObj.month, 1)
    return daysInMonth    

def calendarCreate(dateObj, daysInMonth):
    dateList = []

    for i in range(1, daysInMonth.days + 1):
        dateList.append(date(dateObj.year, dateObj.month, i))
    return dateList

def moveMonthLeft(dateObj):
    if dateObj.month == 1:
        dateObj = date(dateObj.year - 1, 12, dateObj.day)
    else:
        dateObj = date(dateObj.year, dateObj.month - 1, dateObj.day)
    return dateObj

def moveMonthRight(dateObj):
    if dateObj.month == 12:
        dateObj = date(dateObj.year + 1, 1, dateObj.day)
    else:
        dateObj = date(dateObj.year, dateObj.month + 1, dateObj.day)
    return dateObj

def textDisplay(text, x, y):
    font = pygame.font.SysFont("Times New Roman", 30)
    text = font.render(text, False, (0, 0, 0))
    center = gameDisplay.get_rect().center
    gameDisplay.blit(text, (center[0] + x, center[1] + y))
    text.get_rect().center
             
def dayDisplay(dateObj):
    firstDayofWeek = date(dateObj.year, dateObj.month, 1).weekday()
    row = 0
    iteration = firstDayofWeek
    
    for i in range (daysInCurrentMonth(dateObj).days):
        textDisplay(f'{i + 1}', -300 + (97 * iteration), -245 + row * 96)
        iteration += 1
        if((iteration * 99) - 355 > 330):
            row += 1
            iteration = 0
            
def jsonInit():
    jsonfile = open('dates.json')
    jsondict = json.load(jsonfile)
    jsonfile.close()
    return jsondict
            
def calendarTaskView(gameDisplay, dateString):
    broke = False
    string = ""
    jsondict = jsonInit()
    if dateString in jsondict:
       string = jsondict[dateString]
                
    while not broke:
      
        gameDisplay.fill("white")
        calendarView = pygame.image.load(os.path.join(".","images","calendarviewimg2.png"))
        greenArrow = pygame.image.load(os.path.join(".","images","greenarrowcrop.png"))
        gameDisplay.blit(calendarView, [330,40])
        greenArrowBlit = gameDisplay.blit(greenArrow, [350, 675])
        textDisplay(string, -200,-100)
        textDisplay(dateString[7:9], -10,250)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if greenArrowBlit.collidepoint(pygame.mouse.get_pos()):
                    broke = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if string != "":
                        string = string.rstrip(string[-1])
                else:
                    string += event.unicode
        
    if string != "" or dateString in jsondict:
        if dateString not in jsondict:
            jsondict[dateString] = string
        elif string == "":
            del jsondict[dateString]
        else:
            jsondict.update({dateString:string})
        with open ('dates.json', 'w') as file:
            file.write(json.dumps(jsondict))
        

def gameLoop(gameDisplay, calendarList, calendarImg, arrowImg, arrowImgLeft, textBox, dateObj):
    textBoxActive = False
    textBoxText = ""
    while True:
        gameDisplay.fill("white")
        gameDisplay.blit(calendarImg, calendarImg.get_rect(center = gameDisplay.get_rect().center)) #Obtained from StackOverflow
        arrowBlit = gameDisplay.blit(arrowImg, [1000,30])
        leftArrowBlit = gameDisplay.blit(arrowImgLeft, [90,35])
        textBoxBlit = gameDisplay.blit(textBox, [505,590])
        textDisplay(f'{dateObj.month} / {dateObj.year}', -50, -350)
        textDisplay(textBoxText, -100, 240)
        dayDisplay(dateObj)
        pygame.display.flip()
        
        if (textBoxText != "") and (not textBoxActive):
            calendarTaskView(gameDisplay, f"{dateObj.year}-{dateObj.month}-{textBoxText}")
            textBoxText = ""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if leftArrowBlit.collidepoint(pygame.mouse.get_pos()):
                    dateObj = moveMonthLeft(dateObj)
                    calendarList = calendarCreate(dateObj, daysInCurrentMonth(dateObj))
                if arrowBlit.collidepoint(pygame.mouse.get_pos()):
                    dateObj = moveMonthRight(dateObj)
                    calendarList = calendarCreate(dateObj, daysInCurrentMonth(dateObj))
                if textBoxBlit.collidepoint(pygame.mouse.get_pos()):
                    textBoxActive = True;
            if event.type == pygame.KEYDOWN:
                if textBoxActive:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        textBoxActive = False
                    elif event.key == pygame.K_BACKSPACE:
                        if textBoxText != "":
                            textBoxText = textBoxText.rstrip(textBoxText[-1])
                    else:
                        textBoxText += event.unicode
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    dateObj = moveMonthLeft(dateObj)
                    calendarList = calendarCreate(dateObj, daysInCurrentMonth(dateObj))
                if event.key == pygame.K_RIGHT:
                    dateObj = moveMonthRight(dateObj)
                    calendarList = calendarCreate(dateObj, daysInCurrentMonth(dateObj))
        

#General Code and Initilization
pygame.init()
gameDisplay = pygame.display.set_mode((1280,720))
pygame.display.set_caption('calendar Application')
calendarImg = pygame.image.load(os.path.join(".","images","calendardrawingnew.png"))
arrowImg = pygame.image.load(os.path.join(".","images","arrownew.png"))
arrowImgLeft = pygame.transform.flip(arrowImg, 1, 0)
textBox = pygame.image.load(os.path.join(".","images","textboxcropped.png"))
textBox = pygame.transform.scale_by(textBox, 0.9)
calendarList = []
dateObj = datetime.now()
calendarList = calendarCreate(dateObj, daysInCurrentMonth(dateObj))

gameLoop(gameDisplay, calendarList, calendarImg, arrowImg, arrowImgLeft, textBox, dateObj)
    
    
        