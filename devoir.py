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

def devoir_post_it(master, x=780, y=530, canvas_color="#F8F8F8"):
    cm = tkinter.Canvas(master, bg=canvas_color, highlightthickness=0, width=354, height=274)
    cm.place(x=x, y=y)

    ml = ttk.Label(master, text="Devoir", background="#EDC033", font='Helvetica 20 bold')
    ml.place(x=x+93, y=y+40)

    mexit = ttk.Label(master, text="X", background="#EDC033", foreground="#997810", font='Helvetica 15 bold')
    mexit.bind("<Button-1>", lambda uwu: stop(master))
    mexit.place(x=x+248, y=y+4)

    roundPolygon([2, 270, 270, 2], [2, 2, 250, 250], 15 , width=3, outline="#CFA215", fill="#CFA215", canvas=cm)
    roundPolygon([2, 269, 267, 2], [2, 2, 249, 247], 15 , width=2, outline="#EDC033", fill="#EDC033", canvas=cm)

    with open("data.json", "r") as read_file:
        data = json.load(read_file)

    try:
        client = pronotepy.Client("https://0540017a.index-education.net/pronote/eleve.html?login=true", username=data["Identifiant"], password=data["MotDePasse"], ent=data["ent"])
    except:
        print("Identifiant invalide.")
        return
    
    import locale
    locale.setlocale(locale.LC_TIME,'')

    autres = dt.date.today() + dt.timedelta(days=6)
    a = dt.date.today() + dt.timedelta(days=1)
    devoirss = client.homework(a, autres)
    jours = []
    devoirs = []

    for devoir in devoirss:
        jours.append(int(devoir.date.strftime('%d')))

    a = min(jours)

    first = 0
    for devoir in devoirss:
        if int(devoir.date.strftime("%d")) == int(a):
            if first == 0:
                ml2 = ttk.Label(master, text=f"de {devoir.date.strftime('%A')}", background="#EDC033")
                ml2.place(x=x+115, y=y+70)
                first += 1
            devoirs.append(devoir)

    devoir_text = ""
    preload_devoir_text = ""
    lignes = 0
    stop_load = False
    slt = False
    sltc = 30
    preload_ddn = "... "
    preload_wc = 0
    preload_lignes = 0
    for devoir in devoirs:
        ddn = ""
        wc = 0
        dd = devoir.description
        lignes += 3
        for word in dd.split():
            if stop_load == False:
                wc += len(word) + 1
                if lignes == 7 and wc >= 34:
                    ddn += "..."
                    preload_ddn += word + " "
                    preload_wc += len(word) + 1
                    stop_load = True
                    slt = True
                elif wc >= 34:
                    ddn += "\n"
                    wc = len(word) + 1
                    lignes += 1
                
                if stop_load == False:
                    ddn += word + " "
            elif stop_load == True:
                preload_wc += len(word) + 1
                if preload_lignes == 7 and preload_wc >= 34:
                    preload_ddn += "..."
                    break
                elif slt == True and preload_wc >= sltc:
                    preload_ddn += "\n"
                    preload_wc = len(word) + 1
                    preload_lignes += 1
                    sltc = 34
                elif preload_wc >= 34:
                    preload_ddn += "\n"
                    preload_wc = len(word) + 1
                    preload_lignes += 1
                
                preload_ddn += word + " "
        if slt == True:
            preload_devoir_text += preload_ddn + "\n\n"
            preload_lignes += len(preload_ddn.splitlines()) + 1
            preload_ddn = ""
            slt = False
                
        def fonf(value):
            if value is True:
                return "☑"
            else:
                return "☐"

        if lignes == 7 and wc >= 34:
           devoir_text += devoir.subject.name + f" {fonf(devoir.done)}\n- " + ddn
        elif preload_lignes == 7 and preload_wc >= 34:
           preload_devoir_text += devoir.subject.name + f" {fonf(devoir.done)}\n- " + preload_ddn
           break
        elif stop_load == True:
            preload_devoir_text += devoir.subject.name + f" {fonf(devoir.done)}\n- " + preload_ddn + "\n\n"
        else:
            devoir_text += devoir.subject.name + f" {fonf(devoir.done)}\n- " + ddn + "\n\n"
    
    if sum('\n' in item for item in preload_devoir_text) > 7:
        preload_devoir_text = "\n".join(preload_devoir_text.splitlines()[:7])
        
    loaded_label = ttk.Label(cm, text=devoir_text, background="#EDC033", font=("Regular 400", 12))
    loaded_label.place(x=18, y=100)
    preload_loabel = ttk.Label(cm, text=preload_devoir_text, background="#EDC033", font=("Regular 400", 12))

    switch_state = 0

    def switch():
        nonlocal switch_state
        if switch_state == 0:
            loaded_label.place_forget()
            preload_loabel.place(x=18, y=100)
            plus_label.configure(text="Régresser")
            switch_state += 1
        else:
            preload_loabel.place_forget()
            loaded_label.place(x=18, y=100)
            plus_label.configure(text="Développer")
            switch_state = 0

    if stop_load == True:
        plus_label = ttk.Label(cm, text="Développer", background="#EDC033", foreground="#997810", font='Helvetica 7 bold')
        plus_label.bind("<Button-1>", lambda uwu: switch())
        plus_label.place(x=x+115, y=230)

def start_devoir_widget():
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
    devoir_post_it(master=widget, x=0, y=0, canvas_color="red")
    widget.mainloop()

start_devoir_widget()