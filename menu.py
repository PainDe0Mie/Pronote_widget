import tkinter, pronotepy, json
import datetime as dt
from pronotepy.ent import *
from tkinter import ttk

def get_ent(ent):
    if ent == "ac_clermont_ferrand":
        return ac_clermont_ferrand
    elif ent == "ac_grenoble":
        return ac_grenoble
    elif ent == "ac_lyon":
        return ac_lyon
    elif ent == "ac_orleans_tours":
        return ac_orleans_tours
    elif ent == "ac_poitiers":
        return ac_poitiers
    elif ent == "ac_reims":
        return ac_reims
    elif ent == "ac_reunion":
        return ac_reunion
    elif ent == "atrium_sud":
        return atrium_sud
    elif ent == "cas_agora06":
        return cas_agora06
    elif ent == "cas_arsene76":
        return cas_arsene76
    elif ent == "cas_arsene76_edu":
        return cas_arsene76_edu
    elif ent == "cas_cybercolleges42":
        return cas_cybercolleges42
    elif ent == "cas_cybercolleges42_edu":
        return cas_cybercolleges42_edu
    elif ent == "cas_ent27":
        return cas_ent27
    elif ent == "cas_kosmos":
        return cas_kosmos
    elif ent == "cas_seinesaintdenis_edu":
        return cas_seinesaintdenis_edu
    elif ent == "eclat_bfc":
        return eclat_bfc
    elif ent == "ecollege_haute_garonne":
        return ecollege_haute_garonne
    elif ent == "ecollege_haute_garonne_edu":
        return ecollege_haute_garonne_edu
    elif ent == "enc_hauts_de_seine":
        return enc_hauts_de_seine
    elif ent == "ent2d_bordeaux":
        return ent2d_bordeaux
    elif ent == "ent77":
        return ent77
    elif ent == "ent_94":
        return ent_94
    elif ent == "ent_auvergnerhonealpe":
        return ent_auvergnerhonealpe
    elif ent == "ent_creuse":
        return ent_creuse
    elif ent == "ent_elyco":
        return ent_elyco
    elif ent == "ent_essonne":
        return ent_essonne
    elif ent == "ent_hdf":
        return ent_hdf
    elif ent == "ent_mayotte":
        return ent_mayotte
    elif ent == "ent_somme":
        return ent_somme
    elif ent == "ent_var":
        return ent_var
    elif ent == "ile_de_france":
        return ile_de_france
    elif ent == "l_normandie":
        return l_normandie
    elif ent == "laclasse_educonnect":
        return laclasse_educonnect
    elif ent == "laclasse_lyon":
        return laclasse_lyon
    elif ent == "lyceeconnecte_aquitaine":
        return lyceeconnecte_aquitaine
    elif ent == "lyceeconnecte_edu":
        return lyceeconnecte_edu
    elif ent == "monbureaunumerique":
        return monbureaunumerique
    elif ent == "neoconnect_guadeloupe":
        return neoconnect_guadeloupe
    elif ent == "occitanie_montpellier":
        return occitanie_montpellier
    elif ent == "occitanie_montpellier_educonnect":
        return occitanie_montpellier_educonnect
    elif ent == "occitanie_toulouse":
        return occitanie_toulouse
    elif ent == "occitanie_toulouse_edu":
        return occitanie_toulouse_edu
    elif ent == "ozecollege_yvelines":
        return ozecollege_yvelines
    elif ent == "paris_classe_numerique":
        return paris_classe_numerique
    elif ent == "val_doise":
        return val_doise
    elif ent == "extranet_colleges_somme":
        return extranet_colleges_somme

def roundPolygon(x, y, sharpness, canvas, **kwargs):
    if sharpness < 2:
        sharpness = 2

    ratioMultiplier = sharpness - 1
    ratioDividend = sharpness

    points = []

    for i in range(len(x)):
        points.append(x[i])
        points.append(y[i])

        if i != (len(x) - 1):
            points.append((ratioMultiplier*x[i] + x[i + 1])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[i + 1])/ratioDividend)
            points.append((ratioMultiplier*x[i + 1] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[i + 1] + y[i])/ratioDividend)
        else:
            points.append((ratioMultiplier*x[i] + x[0])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[0])/ratioDividend)
            points.append((ratioMultiplier*x[0] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[0] + y[i])/ratioDividend)
            points.append(x[0])
            points.append(y[0])

    return canvas.create_polygon(points, **kwargs, smooth=True)

def stop(master):
    master.destroy()

def menu_post_it(master, x=780, y=530, canvas_color="#F8F8F8"):
    cm = tkinter.Canvas(master, bg=canvas_color, highlightthickness=0, width=354, height=274)
    cm.place(x=x, y=y)

    ml = ttk.Label(master, text="Menu", background="#EDC033", font='Helvetica 20 bold')
    ml.place(x=x+95, y=y+40)

    mexit = ttk.Label(master, text="X", background="#EDC033", foreground="#997810", font='Helvetica 15 bold')
    mexit.bind("<Button-1>", lambda uwu: stop(master))
    mexit.place(x=x+248, y=y+4)

    roundPolygon([2, 270, 270, 2], [2, 2, 250, 250], 15 , width=3, outline="#CFA215", fill="#CFA215", canvas=cm)
    roundPolygon([2, 269, 267, 2], [2, 2, 249, 247], 15 , width=2, outline="#EDC033", fill="#EDC033", canvas=cm)

    with open("data.json", "r") as read_file:
        data = json.load(read_file)

    try:
        client = pronotepy.Client("https://0540017a.index-education.net/pronote/eleve.html?login=true", username=data["Identifiant"], password=data["MotDePasse"], ent=get_ent(data["ent"]))
    except:
        print("Identifiant invalide.")
        return
    
    import locale
    locale.setlocale(locale.LC_TIME,'')

    autres = dt.date.today() + dt.timedelta(days=6)
    menus = client.menus(dt.date.today(), autres)

    for menu in menus:
        ml2 = ttk.Label(master, text=f"de {menu.date.strftime('%A')}", background="#EDC033")
        ml2.place(x=x+105, y=y+70)
        menu_text = ""
        for a in menu.first_meal:
            menu_text += "- " + a.name + "\n"
        for a in menu.main_meal:
            menu_text += "- " + a.name + "\n"
        for a in menu.side_meal:
            menu_text += "- " + a.name + "\n"
        for a in menu.cheese:
            menu_text += "- " + a.name + "\n"
        desserts = ""
        for a in menu.dessert:
            if desserts != "":
                desserts += " / "
                desserts += a.name
            else:
                desserts += "- " + a.name
        menu_text += desserts
        ttk.Label(cm, text=menu_text, background="#EDC033", font=("Regular 400", 12)).place(x=18, y=120)
        break

def start_menu_widget():
    widget = tkinter.Tk()
    widget.overrideredirect(1)
    widget.config(background="red")
    def move_app(e):
        widget.geometry(f'+{e.x_root}+{e.y_root}')
    widget.bind("<B1-Motion>", move_app)
    widget.title("Menu Widget")
    window_height = 274
    window_width = 354
    screen_width = widget.winfo_screenwidth() + 1700
    screen_height = widget.winfo_screenheight() + 700
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    widget.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    widget.lift()
    widget.wm_attributes("-topmost", True)
    widget.wm_attributes("-transparentcolor", "red")
    menu_post_it(master=widget, x=0, y=0, canvas_color="red")
    widget.mainloop()

start_menu_widget()