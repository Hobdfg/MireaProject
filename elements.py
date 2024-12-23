delements = [
    "H - Водороду принадлежит звание самого горячего элемента. В звёздах, включая Солнце, происходят реакции синтеза водорода, выделяющие огромное количество энергии в форме света и тепла.",
    "He - Гелий — один из первых химических элементов, возникших после Большого Взрыва. Наша Вселенная практически на треть состоит из гелия."
]
ptable = {
    1: {"symbol": "H", "name": "Водород", "mass": 1.008, "properties": "Газ, бесцветный, не имеет запаха.", "fact": "Самый распространённый элемент во Вселенной."},
    2: {"symbol": "He", "name": "Гелий", "mass": 4.0026, "properties": "Газ, инертный, бесцветный.", "fact": "Используется в воздушных шарах."},
}
command = ("/start - Запусти или перезапусти бота\n"
            "/commands - Помощь по командам\n"
            "/bot - Запусти режим нейросети\n"
            "/table - Интерактивная таблица Менделеева\n"
            "/daily - Запуск ежедневных интересных фактов про эл-ты химии\n"
            "/formula - Популярные формулы в химии")

simpleformula = ("CaO + H2O = Ca(OH)2 — негашёная известь соединяется с водой, и образуется новое сложное вещество — гашёная известь. 3\n" 
                 "2СО + О2 = 2СО2↑ — оксид углерода (ІІ) + кислород = оксид углерода (IV).\n"
                 "Fe + S = FeS↓ — феррум + сера = сульфид железа (ІІ).\n" 
                 "2Fe + 3Cl2 = 2FeCl3 — феррум + хлор = хлорид железа (ІІІ).\n"  
                 "S + O2 = SO2↑ — сера + кислород = диоксид серы.\n" 
                 "2SO2 + O2 = 2SO3↑ — диоксид серы + кислород = триоксид серы.\n"  
                 "H2 + S = H2S — водород + сера = сероводород.\n"  
                 "SO3 + H2O = H2SO4 — триоксид серы + вода = серная кислота.\n"  
                 "КOH + H2SO4 = KHSO4 — гидроксид калия + серная кислота = гидросульфат калия.\n"  
                 "CaCO3 = CaO + CO2↑ — если нагреть известняк, получаются негашёная известь и углекислый газ.\n"
                 "2Ba + O2 = 2BaO — барий и кислород взаимодействуют с образованием оксида бария.\n"  
                 "Na2O + H2O = 2NaOH — взаимодействие оксида натрия с водой с образованием гидроксида натрия.\n"  
                 "2AgNO3 = 2Ag + 2NO2↑ + O2↑ — разложение нитрата серебра на серебро, оксид азота (IV) и кислород.\n"  
                 "Zn + 2HCl = ZnCl2 + H2↑ — замещение атомов водорода в молекуле соляной кислоты на атомы цинка.\n"  
                 "CaCl2 + Na2CO3 = CaCO3↓ + 2NaCl — при сливании растворов CaCl2 и Na2CO3 выпадает осадок.\n"  
                 "Cu(OH)2 = tCuO + H2O — разложение гидроксида меди на оксид и воду происходит при нагревании.\n"  
                 "H2(г) + Cl2(г) = 2HCl — взаимодействие двух газообразных веществ — водорода и хлора.\n"  
                 "2Na(тв) + 2H2O(ж) = 2NaOH + H2 — реакция между веществами, которые находятся в разных агрегатных состояниях.\n" 
                 "2Ag2O = 4Ag + O2 — разложение оксида серебра на серебро и кислород.\n"  
                 "2Fe(OH)3 = Fe2O3 + 3H2O — разложение гидроксида железа на оксид железа (III) и воду.\n")