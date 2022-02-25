import getpass
from operator import sub
import time

def start():
    for x in range(6):
        
        pw = getpass.getpass()

        """ 
            82 = Geração Y teve início em 1982;
            25 = O Brasil foi reconhecido como nação em 1825;
            12 = Quantidade de notas em uma escala músical cromática;
            07 = O pai da física moderna começa com que letra? (Galileu Galilei / G = 7ª posição);
        """
        if pw == '82251207' :
            print("=========================")
            print(".   PASSWORD ACCEPTED   .")
            print("=========================\n")
            print("SYSTEM: REVEALING THE SECRET PHRASE...")
            print("SYSTEM: WAIT...")
            time.sleep(2)
            print("SYSTEM: WAIT...")
            time.sleep(2)
            print("SYSTEM: WAIT...")
            time.sleep(2)
            print("SYSTEM: WAIT...")
            time.sleep(2)
            print("SYSTEM: WAIT...")
            time.sleep(2)
            print("SYSTEM: WAIT...")
            time.sleep(2)
            print("SYSTEM: SECRET PHRASE: ")
            print('"Independete de onde fomos ou o que somos, o mundo nunca irá brilhar tanto quanto a caréca do Fer..."')
            print("SYSTEM: TURNING OFF SYSTEM...")
            time.sleep(20)
            exit()

        else:
            if x >= 4:
                print("=========================")
                print(".        WARNING        .")
                print("=========================\n")
                print("ERROR: YOU EXCEEDED THE NUMBER OF CHANCES...")
                print("ERROR: THE PROGRAM WILL BE DELETED...\n")
                exit()
            result = 4 - x
            print("=========================")
            print(".        WARNING        .")
            print("=========================\n")
            print("ERROR: WRONG PASSWORD...")
            print("ERROR: YOU HAVE " + str(result) + " MORE ATTEMPTS !!!")
            time.sleep(3)
            forgot = input("\nFORGOT YOUR PASSWORD? (yes/no): ")
            if forgot == "yes":
                if x == 0:
                    print("\n1st TIP: WHEN DID GENERATION Y BEGIN?")
                    time.sleep(3)
                    print("\nALERT: THE PROGRAM WILL RESTART IN 1 MINUTES...\n")
                    time.sleep(60)
                    continue
                elif x == 1:
                    print("\n2nd TIP: THE YEAR WHEN BRAZIL WAS RECOGNIZED AS A NATION.")
                    time.sleep(3)
                    print("\nALERT: THE PROGRAM WILL RESTART IN 1 MINUTES...\n")
                    time.sleep(60)
                    continue
                elif x == 2:
                    print("\n3nd TIP: NUMBER OF MUSICAL NOTES ON A CHROMATIC SCALE")
                    time.sleep(3)
                    print("\nALERT: THE PROGRAM WILL RESTART IN 1 MINUTES...\n")
                    time.sleep(60)
                    continue
                elif x == 3:
                    print("\n4nd TIP: FIRST LETTER OF THE FATHER OF MODERN PHYSICS")
                    time.sleep(3)
                    print("\nALERT: THE PROGRAM WILL RESTART IN 1 MINUTES...\n")
                    time.sleep(60)
                    continue
            elif forgot == 'no':
                continue 




start()