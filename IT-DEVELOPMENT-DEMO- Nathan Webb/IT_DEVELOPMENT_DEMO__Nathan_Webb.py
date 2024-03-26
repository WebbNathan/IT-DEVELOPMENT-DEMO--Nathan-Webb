import pygame, sys,os
from datetime import date, datetime

def calenderCreate(dateObj):
    dateList = []

    firstDayofWeek = date(dateObj.year, dateObj.month, 1).weekday()
    
    if(dateObj.month != 12):
        daysInMonth = date(dateObj.year, dateObj.month + 1, 1) - date(dateObj.year, dateObj.month, 1)
    else:
        daysInMonth = date(dateObj.year + 1, 1, 1) - date(dateObj.year, dateObj.month, 1)

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

def textDisplay():
    font = pygame.font.SysFont("Times New Roman")
    

def calenderDisplay(calenderList, gameDisplay):
    firstDayofWeek = date(dateObj.year, dateObj.month, 1).weekday()
    
    for i in range(len(calenderList)):
        textDisplay()

#standard pygame initialization
pygame.init()
gameDisplay = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Calender Application')
calendarImg = pygame.image.load(os.path.join(".","images","CalendarDrawing.jpg"))
arrowImg = pygame.image.load(os.path.join(".","images","arrow.png"))
arrowImgLeft = pygame.transform.flip(arrowImg, 1, 0)

calenderList = []
dateObj = datetime.now()
calenderList = calenderCreate(dateObj)
print(calenderList)

while True:
    
    gameDisplay.fill("white")
    gameDisplay.blit(calendarImg, calendarImg.get_rect(center = gameDisplay.get_rect().center)) #Obtained from StackOverflow
    arrowBlit = gameDisplay.blit(arrowImg, [650,-285])
    leftArrowBlit = gameDisplay.blit(arrowImgLeft, [-340,-285])
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #This will be user clicking arrows and or grids
            if leftArrowBlit.collidepoint(pygame.mouse.get_pos()):
                dateObj = moveMonthLeft(dateObj)
                calenderList = calenderCreate(dateObj)
                print(calenderList)
            if arrowBlit.collidepoint(pygame.mouse.get_pos()):
                dateObj = moveMonthRight(dateObj)
                calenderList = calenderCreate(dateObj)
                print(calenderList)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_LEFT:
                dateObj = moveMonthLeft(dateObj)
                calenderList = calenderCreate(dateObj)
                print(calenderList)
            if event.key == pygame.K_RIGHT:
                dateObj = moveMonthRight(dateObj)
                calenderList = calenderCreate(dateObj)
                print(calenderList)
    
    
        