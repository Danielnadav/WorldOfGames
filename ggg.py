import random
def GenerateNumber():
    Random_number = random.randint( 1, 100 )
    game = int(GenerateNumber())
    print(game)


    return Random_number
    user_number_file = open("/var/tmp/game.txt", "w+")
    user_number_file.write(str(Random_number))
    user_number_file.write("\n")
    user_number_file.closed
# GenerateNumber()


def get_guess_from_user():
    get_guess_from_user_number = input("User please put you number")


    # user_number_file = open("/var/tmp/game1.txt", "w+")
    # user_number_file.write(get_guess_from_user_number)

get_guess_from_user()
#
#
#
#
# def compare_results():
#
#     m_file = open("/var/tmp/game.txt", "r")
#     m_file1 = m_file.read()
#     #filecmp.cmp = ('game1.txt', 'game2.txt')
#
#     u_file = open("/var/tmp/game1.txt", "r")
#     u_file2 = u_file.read()
#     while u_file2 == m_file1:
#         print("sametttttt")
#     # if u_file2 == m_file1:
#     #     print(" same!!! ")
#     # if m_file1 == u_file2:
#     #     print("SAME\n")
#     else:
#         print("Numbers  not same")
#     # if len(u_file2) == len(set(m_file1)):
#     #     print("same!!! ")
# compare_results()
#
#

