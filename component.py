def menu_dashboard_input():
    menu = int(input("pilih berdasarkan nomor :"))
    if 1 <= menu <=8 :
        return menu
    else : 
        menu_dashboard_input()
        