import pygame, sys,os
from datetime import date, datetime


def daysInCurrentMonth(dateObj):
    if(dateObj.month != 12):
        daysInMonth = date(dateObj.year, dateObj.month + 1, 1) - date(dateObj.year, dateObj.month, 1)
    else:
        daysInMonth = date(dateObj.year + 1, 1, 1) - date(dateObj.year, dateObj.month, 1)
    return daysInMonth    

def calenderCreate(dateObj, daysInMonth):
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
    

def calenderDisplay(calenderList, gameDisplay):
    firstDayofWeek = date(dateObj.year, dateObj.month, 1).weekday()
    
    for i in range(len(calenderList)):
        textDisplay()
        
def dayDisplay(dateObj):
    firstDayofWeek = date(dateObj.year, dateObj.month, 1).weekday()
    row = 0
    iteration = firstDayofWeek
    
    for i in range (daysInCurrentMonth(dateObj).days):
        textDisplay(f'{i + 1}', -355 + (97 * iteration), -245 + row * 96)
        iteration += 1
        if((iteration * 99) - 355 > 330):
            row += 1
            iteration = 0

#standard pygame initialization
pygame.init()
gameDisplay = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Calender Application')
calendarImg = pygame.image.load(os.path.join(".","images","CalendarDrawing.png"))
arrowImg = pygame.image.load(os.path.join(".","images","arrow.png"))
arrowImgLeft = pygame.transform.flip(arrowImg, 1, 0)

calenderList = []
dateObj = datetime.now()
calenderList = calenderCreate(dateObj, daysInCurrentMonth(dateObj))
print(calenderList)

while True:
    
    gameDisplay.fill("white")
    gameDisplay.blit(calendarImg, calendarImg.get_rect(center = gameDisplay.get_rect().center)) #Obtained from StackOverflow
    arrowBlit = gameDisplay.blit(arrowImg, [650,-285])
    leftArrowBlit = gameDisplay.blit(arrowImgLeft, [-340,-285])
    textDisplay(f'{dateObj.month} / {dateObj.year}', -50, -350)
    dayDisplay(dateObj)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #This will be user clicking arrows and or grids
            if leftArrowBlit.collidepoint(pygame.mouse.get_pos()):
                dateObj = moveMonthLeft(dateObj)
                calenderList = calenderCreate(dateObj, daysInCurrentMonth(dateObj))
                print(calenderList)
            if arrowBlit.collidepoint(pygame.mouse.get_pos()):
                dateObj = moveMonthRight(dateObj)
                calenderList = calenderCreate(dateObj, daysInCurrentMonth(dateObj))
                print(calenderList)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_LEFT:
                dateObj = moveMonthLeft(dateObj)
                calenderList = calenderCreate(dateObj, daysInCurrentMonth(dateObj))
                print(calenderList)
            if event.key == pygame.K_RIGHT:
                dateObj = moveMonthRight(dateObj)
                calenderList = calenderCreate(dateObj, daysInCurrentMonth(dateObj))
                print(calenderList)
    
    
        