import dbms as d
print('''
---------------------------------------------------------------------------------------------------------------------------------------------
         Movies and Tv shows are in 'Name,year,quality' format
         And Anime and AnimeMovies are in 'Name, Year, quality '
         
         Type 'exit' - to save and exit the database
         ''')

command = input(''' ''')
running = True
while running:
    if command == "exit" or command =="Exit":
        running = False
    else:
        command = input(''' ''')
    