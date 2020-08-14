# -*- coding: utf-8 -*-
"""
Master Dictionary

Translations
0: English
1: Chinese
2: Dutch
3: French
4: Italian
5: Japanese
6: Korean
7: Portuguese
8: Russian
9: Spanish
"""


class MD_F:
    # Master Dictionary Functions

    def get_languages_list():
        languages = []
        languages.append("English")
        languages.append("Chinese")
        languages.append("Dutch")
        languages.append("French")
        languages.append("Italian")
        languages.append("Japanese")
        languages.append("Korean")
        languages.append("Portuguese")
        languages.append("Russian")
        languages.append("Spanish")
        return languages

    def get_parent_classes_list():
        parent_classes = []
        parent_classes.append("BaseCase")
        parent_classes.append("硒测试用例")
        parent_classes.append("Testgeval")
        parent_classes.append("CasDeBase")
        parent_classes.append("CasoDiProva")
        parent_classes.append("セレニウムテストケース")
        parent_classes.append("셀레늄_테스트_케이스")
        parent_classes.append("CasoDeTeste")
        parent_classes.append("ТестНаСелен")
        parent_classes.append("CasoDePrueba")
        return parent_classes

    def get_masterqa_parent_classes_list():
        parent_classes = []
        parent_classes.append("MasterQA")
        parent_classes.append("MasterQA_中文")
        parent_classes.append("MasterQA_Nederlands")
        parent_classes.append("MasterQA_Français")
        parent_classes.append("MasterQA_Italiano")
        parent_classes.append("MasterQA_日本語")
        parent_classes.append("MasterQA_한국어")
        parent_classes.append("MasterQA_Português")
        parent_classes.append("MasterQA_Русский")
        parent_classes.append("MasterQA_Español")
        return parent_classes

    def get_parent_class_lang(parent_class):
        parent_class_lang = {}
        parent_class_lang["BaseCase"] = "English"
        parent_class_lang["硒测试用例"] = "Chinese"
        parent_class_lang["Testgeval"] = "Dutch"
        parent_class_lang["CasDeBase"] = "French"
        parent_class_lang["CasoDiProva"] = "Italian"
        parent_class_lang["セレニウムテストケース"] = "Japanese"
        parent_class_lang["셀레늄_테스트_케이스"] = "Korean"
        parent_class_lang["CasoDeTeste"] = "Portuguese"
        parent_class_lang["ТестНаСелен"] = "Russian"
        parent_class_lang["CasoDePrueba"] = "Spanish"
        if parent_class not in parent_class_lang.keys():
            raise Exception("Invalid parent_class {%s} not in {%s}!"
                            "" % (parent_class, parent_class_lang.keys()))
        return parent_class_lang[parent_class]

    def get_mqa_par_class_lang(parent_class):
        parent_class_lang = {}
        parent_class_lang["MasterQA"] = "English"
        parent_class_lang["MasterQA_中文"] = "Chinese"
        parent_class_lang["MasterQA_Nederlands"] = "Dutch"
        parent_class_lang["MasterQA_Français"] = "French"
        parent_class_lang["MasterQA_Italiano"] = "Italian"
        parent_class_lang["MasterQA_日本語"] = "Japanese"
        parent_class_lang["MasterQA_한국어"] = "Korean"
        parent_class_lang["MasterQA_Português"] = "Portuguese"
        parent_class_lang["MasterQA_Русский"] = "Russian"
        parent_class_lang["MasterQA_Español"] = "Spanish"
        if parent_class not in parent_class_lang.keys():
            raise Exception("Invalid parent_class {%s} not in {%s}!"
                            "" % (parent_class, parent_class_lang.keys()))
        return parent_class_lang[parent_class]

    def get_lang_parent_class(language):
        lang_parent_class = {}
        lang_parent_class["English"] = "BaseCase"
        lang_parent_class["Chinese"] = "硒测试用例"
        lang_parent_class["Dutch"] = "Testgeval"
        lang_parent_class["French"] = "CasDeBase"
        lang_parent_class["Italian"] = "CasoDiProva"
        lang_parent_class["Japanese"] = "セレニウムテストケース"
        lang_parent_class["Korean"] = "셀레늄_테스트_케이스"
        lang_parent_class["Portuguese"] = "CasoDeTeste"
        lang_parent_class["Russian"] = "ТестНаСелен"
        lang_parent_class["Spanish"] = "CasoDePrueba"
        if language not in lang_parent_class.keys():
            raise Exception("Invalid language {%s} not in {%s}!"
                            "" % (language, lang_parent_class.keys()))
        return lang_parent_class[language]

    def get_mqa_lang_par_class(language):
        lang_parent_class = {}
        lang_parent_class["English"] = "MasterQA"
        lang_parent_class["Chinese"] = "MasterQA_中文"
        lang_parent_class["Dutch"] = "MasterQA_Nederlands"
        lang_parent_class["French"] = "MasterQA_Français"
        lang_parent_class["Italian"] = "MasterQA_Italiano"
        lang_parent_class["Japanese"] = "MasterQA_日本語"
        lang_parent_class["Korean"] = "MasterQA_한국어"
        lang_parent_class["Portuguese"] = "MasterQA_Português"
        lang_parent_class["Russian"] = "MasterQA_Русский"
        lang_parent_class["Spanish"] = "MasterQA_Español"
        if language not in lang_parent_class.keys():
            raise Exception("Invalid language {%s} not in {%s}!"
                            "" % (language, lang_parent_class.keys()))
        return lang_parent_class[language]

    def get_import_line(language):
        import_line = {}
        # - The Default Import Line:
        import_line["English"] = (
            "from seleniumbase import BaseCase")
        # - Translated Import Lines:
        import_line["Chinese"] = (
            "from seleniumbase.translate.chinese import 硒测试用例")
        import_line["Dutch"] = (
            "from seleniumbase.translate.dutch import Testgeval")
        import_line["French"] = (
            "from seleniumbase.translate.french import CasDeBase")
        import_line["Italian"] = (
            "from seleniumbase.translate.italian import CasoDiProva")
        import_line["Japanese"] = (
            "from seleniumbase.translate.japanese import セレニウムテストケース")
        import_line["Korean"] = (
            "from seleniumbase.translate.korean import 셀레늄_테스트_케이스")
        import_line["Portuguese"] = (
            "from seleniumbase.translate.portuguese import CasoDeTeste")
        import_line["Russian"] = (
            "from seleniumbase.translate.russian import ТестНаСелен")
        import_line["Spanish"] = (
            "from seleniumbase.translate.spanish import CasoDePrueba")
        if language not in import_line.keys():
            raise Exception("Invalid language {%s} not in {%s}!"
                            "" % (language, import_line.keys()))
        return import_line[language]

    def get_mqa_im_line(language):
        import_line = {}
        # - The Default Import Line:
        import_line["English"] = (
            "from seleniumbase import MasterQA")
        # - Translated Import Lines:
        import_line["Chinese"] = (
            "from seleniumbase.translate.chinese import MasterQA_中文")
        import_line["Dutch"] = (
            "from seleniumbase.translate.dutch import MasterQA_Nederlands")
        import_line["French"] = (
            "from seleniumbase.translate.french import MasterQA_Français")
        import_line["Italian"] = (
            "from seleniumbase.translate.italian import MasterQA_Italiano")
        import_line["Japanese"] = (
            "from seleniumbase.translate.japanese import MasterQA_日本語")
        import_line["Korean"] = (
            "from seleniumbase.translate.korean import MasterQA_한국어")
        import_line["Portuguese"] = (
            "from seleniumbase.translate.portuguese import MasterQA_Português")
        import_line["Russian"] = (
            "from seleniumbase.translate.russian import MasterQA_Русский")
        import_line["Spanish"] = (
            "from seleniumbase.translate.spanish import MasterQA_Español")
        if language not in import_line.keys():
            raise Exception("Invalid language {%s} not in {%s}!"
                            "" % (language, import_line.keys()))
        return import_line[language]

    def get_locale_code(language):
        locale_codes = {}
        locale_codes["English"] = "en"
        locale_codes["Chinese"] = "zh"
        locale_codes["Dutch"] = "nl"
        locale_codes["French"] = "fr"
        locale_codes["Italian"] = "it"
        locale_codes["Japanese"] = "ja"
        locale_codes["Korean"] = "ko"
        locale_codes["Portuguese"] = "pt"
        locale_codes["Russian"] = "ru"
        locale_codes["Spanish"] = "es"
        if language not in locale_codes.keys():
            raise Exception("Invalid language {%s} not in {%s}!"
                            "" % (language, locale_codes.keys()))
        return locale_codes[language]

    def get_locale_list():
        locale_list = []
        locale_list.append("en")
        locale_list.append("zh")
        locale_list.append("nl")
        locale_list.append("fr")
        locale_list.append("it")
        locale_list.append("ja")
        locale_list.append("ko")
        locale_list.append("pt")
        locale_list.append("ru")
        locale_list.append("es")
        return locale_list


class MD_L_Codes:
    # Master Dictionary Language Codes
    lang = {}
    lang["English"] = 0
    lang["Chinese"] = 1
    lang["Dutch"] = 2
    lang["French"] = 3
    lang["Italian"] = 4
    lang["Japanese"] = 5
    lang["Korean"] = 6
    lang["Portuguese"] = 7
    lang["Russian"] = 8
    lang["Spanish"] = 9


class MD:
    # Master Dictionary
    md = {}
    num_langs = len(MD_L_Codes.lang)

    md["open"] = ["*"] * num_langs
    md["open"][0] = "open"
    md["open"][1] = "开启"
    md["open"][2] = "openen"
    md["open"][3] = "ouvrir"
    md["open"][4] = "apri"
    md["open"][5] = "を開く"
    md["open"][6] = "열기"
    md["open"][7] = "abrir"
    md["open"][8] = "открыть"
    md["open"][9] = "abrir"

    md["open_url"] = ["*"] * num_langs
    md["open_url"][0] = "open_url"
    md["open_url"][1] = "开启网址"
    md["open_url"][2] = "url_openen"
    md["open_url"][3] = "ouvrir_url"
    md["open_url"][4] = "apri_url"
    md["open_url"][5] = "URLを開く"
    md["open_url"][6] = "URL_열기"
    md["open_url"][7] = "abrir_url"
    md["open_url"][8] = "открыть_URL"
    md["open_url"][9] = "abrir_url"

    md["click"] = ["*"] * num_langs
    md["click"][0] = "click"
    md["click"][1] = "单击"
    md["click"][2] = "klik"
    md["click"][3] = "cliquer"
    md["click"][4] = "fare_clic"
    md["click"][5] = "クリックして"
    md["click"][6] = "클릭"
    md["click"][7] = "clique"
    md["click"][8] = "нажмите"
    md["click"][9] = "haga_clic"

    md["double_click"] = ["*"] * num_langs
    md["double_click"][0] = "double_click"
    md["double_click"][1] = "双击"
    md["double_click"][2] = "dubbelklik"
    md["double_click"][3] = "double_cliquer"
    md["double_click"][4] = "doppio_clic"
    md["double_click"][5] = "ダブルクリックして"
    md["double_click"][6] = "더블_클릭"
    md["double_click"][7] = "clique_duas_vezes"
    md["double_click"][8] = "дважды_нажмите"
    md["double_click"][9] = "doble_clic"

    md["slow_click"] = ["*"] * num_langs
    md["slow_click"][0] = "slow_click"
    md["slow_click"][1] = "慢单击"
    md["slow_click"][2] = "klik_langzaam"
    md["slow_click"][3] = "cliquer_lentement"
    md["slow_click"][4] = "clicca_lentamente"
    md["slow_click"][5] = "ゆっくりクリックして"
    md["slow_click"][6] = "천천히_클릭"
    md["slow_click"][7] = "clique_devagar"
    md["slow_click"][8] = "нажмите_медленно"
    md["slow_click"][9] = "haga_clic_lentamente"

    md["click_link_text"] = ["*"] * num_langs
    md["click_link_text"][0] = "click_link_text"
    md["click_link_text"][1] = "单击链接文本"
    md["click_link_text"][2] = "klik_linktekst"
    md["click_link_text"][3] = "cliquer_texte_du_lien"
    md["click_link_text"][4] = "fare_clic_testo_del_collegamento"
    md["click_link_text"][5] = "リンクテキストをクリックします"
    md["click_link_text"][6] = "링크_텍스트를_클릭합니다"
    md["click_link_text"][7] = "clique_texto_do_link"
    md["click_link_text"][8] = "нажмите_ссылку"
    md["click_link_text"][9] = "haga_clic_texto_del_enlace"

    md["update_text"] = ["*"] * num_langs
    md["update_text"][0] = "update_text"
    md["update_text"][1] = "更新文本"
    md["update_text"][2] = "tekst_bijwerken"
    md["update_text"][3] = "modifier_texte"
    md["update_text"][4] = "aggiornare_testo"
    md["update_text"][5] = "テキストを更新"
    md["update_text"][6] = "텍스트를_업데이트"
    md["update_text"][7] = "atualizar_texto"
    md["update_text"][8] = "обновить_текст"
    md["update_text"][9] = "actualizar_texto"

    md["add_text"] = ["*"] * num_langs
    md["add_text"][0] = "add_text"
    md["add_text"][1] = "添加文本"
    md["add_text"][2] = "tekst_toevoegen"
    md["add_text"][3] = "ajouter_texte"
    md["add_text"][4] = "aggiungi_testo"
    md["add_text"][5] = "テキストを追加"
    md["add_text"][6] = "텍스트를_추가"
    md["add_text"][7] = "adicionar_texto"
    md["add_text"][8] = "добавить_текст"
    md["add_text"][9] = "agregar_texto"

    md["get_text"] = ["*"] * num_langs
    md["get_text"][0] = "get_text"
    md["get_text"][1] = "获取文本"
    md["get_text"][2] = "tekst_ophalen"
    md["get_text"][3] = "obtenir_texte"
    md["get_text"][4] = "ottenere_testo"
    md["get_text"][5] = "テキストを取得"
    md["get_text"][6] = "텍스트를_검색"
    md["get_text"][7] = "obter_texto"
    md["get_text"][8] = "получить_текст"
    md["get_text"][9] = "obtener_texto"

    md["assert_text"] = ["*"] * num_langs
    md["assert_text"][0] = "assert_text"
    md["assert_text"][1] = "断言文本"
    md["assert_text"][2] = "controleren_tekst"
    md["assert_text"][3] = "vérifier_texte"
    md["assert_text"][4] = "verificare_testo"
    md["assert_text"][5] = "テキストを確認する"
    md["assert_text"][6] = "텍스트_확인"
    md["assert_text"][7] = "verificar_texto"
    md["assert_text"][8] = "подтвердить_текст"
    md["assert_text"][9] = "verificar_texto"

    md["assert_exact_text"] = ["*"] * num_langs
    md["assert_exact_text"][0] = "assert_exact_text"
    md["assert_exact_text"][1] = "确切断言文本"
    md["assert_exact_text"][2] = "controleren_exacte_tekst"
    md["assert_exact_text"][3] = "vérifier_exactement_texte"
    md["assert_exact_text"][4] = "verificare_testo_esatto"
    md["assert_exact_text"][5] = "正確なテキストを確認する"
    md["assert_exact_text"][6] = "정확한_텍스트를_확인하는"
    md["assert_exact_text"][7] = "verificar_texto_exato"
    md["assert_exact_text"][8] = "подтвердить_текст_точно"
    md["assert_exact_text"][9] = "verificar_texto_exacto"

    md["assert_link_text"] = ["*"] * num_langs
    md["assert_link_text"][0] = "assert_link_text"
    md["assert_link_text"][1] = "断言链接文本"
    md["assert_link_text"][2] = "controleren_linktekst"
    md["assert_link_text"][3] = "vérifier_texte_du_lien"
    md["assert_link_text"][4] = "verificare_testo_del_collegamento"
    md["assert_link_text"][5] = "リンクテキストを確認する"
    md["assert_link_text"][6] = "링크_텍스트_확인"
    md["assert_link_text"][7] = "verificar_texto_do_link"
    md["assert_link_text"][8] = "подтвердить_ссылку"
    md["assert_link_text"][9] = "verificar_texto_del_enlace"

    md["assert_element"] = ["*"] * num_langs
    md["assert_element"][0] = "assert_element"
    md["assert_element"][1] = "断言元素"
    md["assert_element"][2] = "controleren_element"
    md["assert_element"][3] = "vérifier_élément"
    md["assert_element"][4] = "verificare_elemento"
    md["assert_element"][5] = "要素を確認する"
    md["assert_element"][6] = "요소_확인"
    md["assert_element"][7] = "verificar_elemento"
    md["assert_element"][8] = "подтвердить_элемент"
    md["assert_element"][9] = "verificar_elemento"

    md["assert_element_visible"] = ["*"] * num_langs
    md["assert_element_visible"][0] = "assert_element_visible"
    md["assert_element_visible"][1] = "断言元素可见"
    md["assert_element_visible"][2] = "controleren_element_zichtbaar"
    md["assert_element_visible"][3] = "vérifier_élément_affiché"
    md["assert_element_visible"][4] = "verificare_elemento_visto"
    md["assert_element_visible"][5] = "要素が表示されていることを確認"
    md["assert_element_visible"][6] = "요소가_보이는지_확인"
    md["assert_element_visible"][7] = "verificar_elemento_visível"
    md["assert_element_visible"][8] = "подтвердить_элемент_виден"
    md["assert_element_visible"][9] = "verificar_elemento_se_muestre"

    md["assert_element_not_visible"] = ["*"] * num_langs
    md["assert_element_not_visible"][0] = "assert_element_not_visible"
    md["assert_element_not_visible"][1] = "断言元素不可见"
    md["assert_element_not_visible"][2] = "controleren_element_niet_zichtbaar"
    md["assert_element_not_visible"][3] = "vérifier_élément_pas_affiché"
    md["assert_element_not_visible"][4] = "verificare_elemento_non_visto"
    md["assert_element_not_visible"][5] = "要素が表示されていないことを確認します"
    md["assert_element_not_visible"][6] = "요소가_보이지_않는지_확인"
    md["assert_element_not_visible"][7] = "verificar_elemento_não_visível"
    md["assert_element_not_visible"][8] = "подтвердить_элемент_не_виден"
    md["assert_element_not_visible"][9] = "verificar_elemento_no_se_muestre"

    md["assert_element_present"] = ["*"] * num_langs
    md["assert_element_present"][0] = "assert_element_present"
    md["assert_element_present"][1] = "断言元素存在"
    md["assert_element_present"][2] = "controleren_element_aanwezig"
    md["assert_element_present"][3] = "vérifier_élément_présent"
    md["assert_element_present"][4] = "verificare_elemento_presente"
    md["assert_element_present"][5] = "要素が存在することを確認します"
    md["assert_element_present"][6] = "요소가_존재하는지_확인"
    md["assert_element_present"][7] = "verificar_elemento_presente"
    md["assert_element_present"][8] = "подтвердить_элемент_присутствует"
    md["assert_element_present"][9] = "verificar_elemento_presente"

    md["assert_element_absent"] = ["*"] * num_langs
    md["assert_element_absent"][0] = "assert_element_absent"
    md["assert_element_absent"][1] = "断言元素不存在"
    md["assert_element_absent"][2] = "controleren_element_afwezig"
    md["assert_element_absent"][3] = "vérifier_élément_pas_présent"
    md["assert_element_absent"][4] = "verificare_elemento_assente"
    md["assert_element_absent"][5] = "要素が存在しないことを確認します"
    md["assert_element_absent"][6] = "요소가_존재하지_않는지_확인"
    md["assert_element_absent"][7] = "verificar_elemento_ausente"
    md["assert_element_absent"][8] = "подтвердить_элемент_отсутствует"
    md["assert_element_absent"][9] = "verificar_elemento_ausente"

    md["assert_title"] = ["*"] * num_langs
    md["assert_title"][0] = "assert_title"
    md["assert_title"][1] = "断言标题"
    md["assert_title"][2] = "controleren_titel"
    md["assert_title"][3] = "vérifier_titre"
    md["assert_title"][4] = "verificare_titolo"
    md["assert_title"][5] = "タイトルを確認"
    md["assert_title"][6] = "제목_확인"
    md["assert_title"][7] = "verificar_título"
    md["assert_title"][8] = "подтвердить_название"
    md["assert_title"][9] = "verificar_título"

    md["get_title"] = ["*"] * num_langs
    md["get_title"][0] = "get_title"
    md["get_title"][1] = "获取标题"
    md["get_title"][2] = "titel_ophalen"
    md["get_title"][3] = "obtenir_titre"
    md["get_title"][4] = "ottenere_titolo"
    md["get_title"][5] = "タイトルを取得する"
    md["get_title"][6] = "제목_검색"
    md["get_title"][7] = "obter_título"
    md["get_title"][8] = "получить_название"
    md["get_title"][9] = "obtener_título"

    md["assert_true"] = ["*"] * num_langs
    md["assert_true"][0] = "assert_true"
    md["assert_true"][1] = "断言为真"
    md["assert_true"][2] = "controleren_ware"
    md["assert_true"][3] = "vérifier_vrai"
    md["assert_true"][4] = "verificare_vero"
    md["assert_true"][5] = "検証が正しい"
    md["assert_true"][6] = "올바른지_확인"
    md["assert_true"][7] = "verificar_verdade"
    md["assert_true"][8] = "подтвердить_правду"
    md["assert_true"][9] = "verificar_verdad"

    md["assert_false"] = ["*"] * num_langs
    md["assert_false"][0] = "assert_false"
    md["assert_false"][1] = "断言为假"
    md["assert_false"][2] = "controleren_valse"
    md["assert_false"][3] = "vérifier_faux"
    md["assert_false"][4] = "verificare_falso"
    md["assert_false"][5] = "検証は偽です"
    md["assert_false"][6] = "거짓인지_확인"
    md["assert_false"][7] = "verificar_falso"
    md["assert_false"][8] = "подтвердить_ложные"
    md["assert_false"][9] = "verificar_falso"

    md["assert_equal"] = ["*"] * num_langs
    md["assert_equal"][0] = "assert_equal"
    md["assert_equal"][1] = "断言等于"
    md["assert_equal"][2] = "controleren_gelijk"
    md["assert_equal"][3] = "vérifier_égal"
    md["assert_equal"][4] = "verificare_uguale"
    md["assert_equal"][5] = "検証が等しい"
    md["assert_equal"][6] = "동일한지_확인"
    md["assert_equal"][7] = "verificar_igual"
    md["assert_equal"][8] = "подтвердить_одинаковый"
    md["assert_equal"][9] = "verificar_igual"

    md["assert_not_equal"] = ["*"] * num_langs
    md["assert_not_equal"][0] = "assert_not_equal"
    md["assert_not_equal"][1] = "断言不等于"
    md["assert_not_equal"][2] = "controleren_niet_gelijk"
    md["assert_not_equal"][3] = "vérifier_non_égal"
    md["assert_not_equal"][4] = "verificare_non_uguale"
    md["assert_not_equal"][5] = "検証が等しくない"
    md["assert_not_equal"][6] = "동일하지_않다고_어설션"
    md["assert_not_equal"][7] = "verificar_não_igual"
    md["assert_not_equal"][8] = "подтвердить_не_одинаковый"
    md["assert_not_equal"][9] = "verificar_diferente"

    md["refresh_page"] = ["*"] * num_langs
    md["refresh_page"][0] = "refresh_page"
    md["refresh_page"][1] = "刷新页面"
    md["refresh_page"][2] = "ververs_pagina"
    md["refresh_page"][3] = "rafraîchir_la_page"
    md["refresh_page"][4] = "aggiorna_la_pagina"
    md["refresh_page"][5] = "ページを更新する"
    md["refresh_page"][6] = "페이지_새로_고침"
    md["refresh_page"][7] = "atualizar_a_página"
    md["refresh_page"][8] = "обновить_страницу"
    md["refresh_page"][9] = "actualizar_la_página"

    md["get_current_url"] = ["*"] * num_langs
    md["get_current_url"][0] = "get_current_url"
    md["get_current_url"][1] = "获取当前网址"
    md["get_current_url"][2] = "huidige_url_ophalen"
    md["get_current_url"][3] = "obtenir_url_actuelle"
    md["get_current_url"][4] = "ottenere_url_corrente"
    md["get_current_url"][5] = "現在のURLを取得"
    md["get_current_url"][6] = "현재의_URL을_가져"
    md["get_current_url"][7] = "obter_url_atual"
    md["get_current_url"][8] = "получить_текущий_URL"
    md["get_current_url"][9] = "obtener_url_actual"

    md["get_page_source"] = ["*"] * num_langs
    md["get_page_source"][0] = "get_page_source"
    md["get_page_source"][1] = "获取页面源代码"
    md["get_page_source"][2] = "broncode_ophalen"
    md["get_page_source"][3] = "obtenir_html_de_la_page"
    md["get_page_source"][4] = "ottenere_la_pagina_html"
    md["get_page_source"][5] = "ページのソースコードを取得する"
    md["get_page_source"][6] = "페이지의_소스_코드를_얻을"
    md["get_page_source"][7] = "obter_a_página_html"
    md["get_page_source"][8] = "получить_источник_страницы"
    md["get_page_source"][9] = "obtener_html_de_la_página"

    md["go_back"] = ["*"] * num_langs
    md["go_back"][0] = "go_back"
    md["go_back"][1] = "回去"
    md["go_back"][2] = "terug"
    md["go_back"][3] = "retour"
    md["go_back"][4] = "indietro"
    md["go_back"][5] = "戻る"
    md["go_back"][6] = "뒤로"
    md["go_back"][7] = "voltar"
    md["go_back"][8] = "назад"
    md["go_back"][9] = "volver"

    md["go_forward"] = ["*"] * num_langs
    md["go_forward"][0] = "go_forward"
    md["go_forward"][1] = "向前"
    md["go_forward"][2] = "vooruit"
    md["go_forward"][3] = "en_avant"
    md["go_forward"][4] = "avanti"
    md["go_forward"][5] = "進む"
    md["go_forward"][6] = "앞으로"
    md["go_forward"][7] = "avançar"
    md["go_forward"][8] = "вперед"
    md["go_forward"][9] = "adelante"

    md["is_text_visible"] = ["*"] * num_langs
    md["is_text_visible"][0] = "is_text_visible"
    md["is_text_visible"][1] = "文本是否显示"
    md["is_text_visible"][2] = "tekst_zichtbaar"
    md["is_text_visible"][3] = "est_texte_affiché"
    md["is_text_visible"][4] = "è_testo_visto"
    md["is_text_visible"][5] = "テキストが表示されています"
    md["is_text_visible"][6] = "텍스트가_표시됩니다"
    md["is_text_visible"][7] = "o_texto_está_visível"
    md["is_text_visible"][8] = "текст_виден"
    md["is_text_visible"][9] = "se_muestra_el_texto"

    md["is_element_visible"] = ["*"] * num_langs
    md["is_element_visible"][0] = "is_element_visible"
    md["is_element_visible"][1] = "元素是否可见"
    md["is_element_visible"][2] = "element_zichtbaar"
    md["is_element_visible"][3] = "est_un_élément_affiché"
    md["is_element_visible"][4] = "è_elemento_visto"
    md["is_element_visible"][5] = "要素は表示されますか"
    md["is_element_visible"][6] = "요소가_표시됩니다"
    md["is_element_visible"][7] = "o_elemento_está_visível"
    md["is_element_visible"][8] = "элемент_виден"
    md["is_element_visible"][9] = "se_muestra_el_elemento"

    md["is_element_present"] = ["*"] * num_langs
    md["is_element_present"][0] = "is_element_present"
    md["is_element_present"][1] = "元素是否存在"
    md["is_element_present"][2] = "element_aanwezig"
    md["is_element_present"][3] = "est_un_élément_présent"
    md["is_element_present"][4] = "è_elemento_presente"
    md["is_element_present"][5] = "要素が存在するかどうか"
    md["is_element_present"][6] = "요소가_있습니다"
    md["is_element_present"][7] = "o_elemento_está_presente"
    md["is_element_present"][8] = "элемент_присутствует"
    md["is_element_present"][9] = "está_presente_el_elemento"

    md["wait_for_text"] = ["*"] * num_langs
    md["wait_for_text"][0] = "wait_for_text"
    md["wait_for_text"][1] = "等待文本"
    md["wait_for_text"][2] = "wachten_op_tekst"
    md["wait_for_text"][3] = "attendre_le_texte"
    md["wait_for_text"][4] = "attendere_il_testo"
    md["wait_for_text"][5] = "テキストを待つ"
    md["wait_for_text"][6] = "텍스트가_나타날_때까지_기다립니다"
    md["wait_for_text"][7] = "aguardar_o_texto"
    md["wait_for_text"][8] = "ждать_текста"
    md["wait_for_text"][9] = "espera_el_texto"

    md["wait_for_element"] = ["*"] * num_langs
    md["wait_for_element"][0] = "wait_for_element"
    md["wait_for_element"][1] = "等待元素"
    md["wait_for_element"][2] = "wachten_op_element"
    md["wait_for_element"][3] = "attendre_un_élément"
    md["wait_for_element"][4] = "attendere_un_elemento"
    md["wait_for_element"][5] = "要素を待つ"
    md["wait_for_element"][6] = "요소가_나타날_때까지_기다립니다"
    md["wait_for_element"][7] = "aguardar_o_elemento"
    md["wait_for_element"][8] = "ждать_элемента"
    md["wait_for_element"][9] = "espera_el_elemento"

    md["wait_for_element_visible"] = ["*"] * num_langs
    md["wait_for_element_visible"][0] = "wait_for_element_visible"
    md["wait_for_element_visible"][1] = "等待元素可见"
    md["wait_for_element_visible"][2] = "wachten_op_element_zichtbaar"
    md["wait_for_element_visible"][3] = "attendre_un_élément_affiché"
    md["wait_for_element_visible"][4] = "attendere_un_elemento_visto"
    md["wait_for_element_visible"][5] = "要素が表示されるのを待ちます"
    md["wait_for_element_visible"][6] = "요소가_표시_될_때까지_기다립니다"
    md["wait_for_element_visible"][7] = "aguardar_o_elemento_visível"
    md["wait_for_element_visible"][8] = "ждать_элемента_виден"
    md["wait_for_element_visible"][9] = "espera_el_elemento_se_muestre"

    md["wait_for_element_not_visible"] = ["*"] * num_langs
    md["wait_for_element_not_visible"][0] = "wait_for_element_not_visible"
    md["wait_for_element_not_visible"][1] = "等待元素不可见"
    md["wait_for_element_not_visible"][2] = "wachten_op_element_niet_zichtbaar"
    md["wait_for_element_not_visible"][3] = "attendre_un_élément_pas_affiché"
    md["wait_for_element_not_visible"][4] = "attendere_un_elemento_non_visto"
    md["wait_for_element_not_visible"][5] = "要素が表示されなくなるまで待ちます"
    md["wait_for_element_not_visible"][6] = "요소가_사라질_때까지_기다리십시오"
    md["wait_for_element_not_visible"][7] = "aguardar_o_elemento_não_visível"
    md["wait_for_element_not_visible"][8] = "ждать_элемента_не_виден"
    md["wait_for_element_not_visible"][9] = "espera_el_elemento_no_se_muestre"

    md["wait_for_element_present"] = ["*"] * num_langs
    md["wait_for_element_present"][0] = "wait_for_element_present"
    md["wait_for_element_present"][1] = "等待元素存在"
    md["wait_for_element_present"][2] = "wachten_op_element_aanwezig"
    md["wait_for_element_present"][3] = "attendre_un_élément_présent"
    md["wait_for_element_present"][4] = "attendere_un_elemento_presente"
    md["wait_for_element_present"][5] = "要素が存在するのを待つ"
    md["wait_for_element_present"][6] = "요소가_존재할_때까지_기다립니다"
    md["wait_for_element_present"][7] = "aguardar_o_elemento_presente"
    md["wait_for_element_present"][8] = "ждать_элемента_присутствует"
    md["wait_for_element_present"][9] = "espera_el_elemento_presente"

    md["wait_for_element_absent"] = ["*"] * num_langs
    md["wait_for_element_absent"][0] = "wait_for_element_absent"
    md["wait_for_element_absent"][1] = "等待元素不存在"
    md["wait_for_element_absent"][2] = "wachten_op_element_afwezig"
    md["wait_for_element_absent"][3] = "attendre_un_élément_pas_présent"
    md["wait_for_element_absent"][4] = "attendere_un_elemento_assente"
    md["wait_for_element_absent"][5] = "要素が存在しないのを待つ"
    md["wait_for_element_absent"][6] = "요소가_나타날_때까지_기다리십시오"
    md["wait_for_element_absent"][7] = "aguardar_o_elemento_ausente"
    md["wait_for_element_absent"][8] = "ждать_элемента_отсутствует"
    md["wait_for_element_absent"][9] = "espera_el_elemento_ausente"

    md["sleep"] = ["*"] * num_langs
    md["sleep"][0] = "sleep"
    md["sleep"][1] = "睡"
    md["sleep"][2] = "slapen"
    md["sleep"][3] = "dormir"
    md["sleep"][4] = "dormire"
    md["sleep"][5] = "眠る"
    md["sleep"][6] = "잠을"
    md["sleep"][7] = "dormir"
    md["sleep"][8] = "спать"
    md["sleep"][9] = "dormir"

    md["wait"] = ["*"] * num_langs
    md["wait"][0] = "wait"
    md["wait"][1] = "等待"
    md["wait"][2] = "wachten"
    md["wait"][3] = "attendre"
    md["wait"][4] = "attendere"
    md["wait"][5] = "待つ"
    md["wait"][6] = "기다림"
    md["wait"][7] = "aguardar"
    md["wait"][8] = "ждать"
    md["wait"][9] = "espera"

    md["submit"] = ["*"] * num_langs
    md["submit"][0] = "submit"
    md["submit"][1] = "提交"
    md["submit"][2] = "verzenden"
    md["submit"][3] = "soumettre"
    md["submit"][4] = "inviare"
    md["submit"][5] = "を提出す"
    md["submit"][6] = "제출"
    md["submit"][7] = "enviar"
    md["submit"][8] = "отправить"
    md["submit"][9] = "enviar"

    md["js_click"] = ["*"] * num_langs
    md["js_click"][0] = "js_click"
    md["js_click"][1] = "JS单击"
    md["js_click"][2] = "js_klik"
    md["js_click"][3] = "js_clic"
    md["js_click"][4] = "js_fare_clic"
    md["js_click"][5] = "JSクリックして"
    md["js_click"][6] = "JS_클릭"
    md["js_click"][7] = "js_clique"
    md["js_click"][8] = "JS_нажмите"
    md["js_click"][9] = "js_haga_clic"

    md["js_update_text"] = ["*"] * num_langs
    md["js_update_text"][0] = "js_update_text"
    md["js_update_text"][1] = "JS更新文本"
    md["js_update_text"][2] = "js_tekst_bijwerken"
    md["js_update_text"][3] = "js_modifier_texte"
    md["js_update_text"][4] = "js_aggiornare_testo"
    md["js_update_text"][5] = "JSテキストを更新"
    md["js_update_text"][6] = "JS_텍스트를_업데이트"
    md["js_update_text"][7] = "js_atualizar_texto"
    md["js_update_text"][8] = "JS_обновить_текст"
    md["js_update_text"][9] = "js_actualizar_texto"

    md["js_type"] = ["*"] * num_langs
    md["js_type"][0] = "js_type"
    md["js_type"][1] = "JS输入文本"
    md["js_type"][2] = "js_typ"
    md["js_type"][3] = "js_taper"
    md["js_type"][4] = "js_digitare"
    md["js_type"][5] = "JS入力"
    md["js_type"][6] = "JS_입력"
    md["js_type"][7] = "js_tipo"
    md["js_type"][8] = "JS_введите"
    md["js_type"][9] = "js_escriba"

    md["inspect_html"] = ["*"] * num_langs
    md["inspect_html"][0] = "inspect_html"
    md["inspect_html"][1] = "检查HTML"
    md["inspect_html"][2] = "html_inspecteren"
    md["inspect_html"][3] = "vérifier_html"
    md["inspect_html"][4] = "controlla_html"
    md["inspect_html"][5] = "HTMLをチェック"
    md["inspect_html"][6] = "HTML_확인"
    md["inspect_html"][7] = "verificar_html"
    md["inspect_html"][8] = "проверить_HTML"
    md["inspect_html"][9] = "comprobar_html"

    md["save_screenshot"] = ["*"] * num_langs
    md["save_screenshot"][0] = "save_screenshot"
    md["save_screenshot"][1] = "保存截图"
    md["save_screenshot"][2] = "bewaar_screenshot"
    md["save_screenshot"][3] = "enregistrer_capture_d_écran"
    md["save_screenshot"][4] = "salva_screenshot"
    md["save_screenshot"][5] = "スクリーンショットを保存"
    md["save_screenshot"][6] = "스크린_샷_저장"
    md["save_screenshot"][7] = "salvar_captura_de_tela"
    md["save_screenshot"][8] = "сохранить_скриншот"
    md["save_screenshot"][9] = "guardar_captura_de_pantalla"

    md["choose_file"] = ["*"] * num_langs
    md["choose_file"][0] = "choose_file"
    md["choose_file"][1] = "选择文件"
    md["choose_file"][2] = "selecteer_bestand"
    md["choose_file"][3] = "sélectionner_fichier"
    md["choose_file"][4] = "seleziona_file"
    md["choose_file"][5] = "ファイルを選択"
    md["choose_file"][6] = "파일을_선택"
    md["choose_file"][7] = "selecionar_arquivo"
    md["choose_file"][8] = "выберите_файл"
    md["choose_file"][9] = "seleccionar_archivo"

    md["execute_script"] = ["*"] * num_langs
    md["execute_script"][0] = "execute_script"
    md["execute_script"][1] = "执行脚本"
    md["execute_script"][2] = "voer_het_script_uit"
    md["execute_script"][3] = "exécuter_le_script"
    md["execute_script"][4] = "esegui_script"
    md["execute_script"][5] = "スクリプトを実行する"
    md["execute_script"][6] = "스크립트를_실행하려면"
    md["execute_script"][7] = "executar_o_script"
    md["execute_script"][8] = "выполнить_скрипт"
    md["execute_script"][9] = "ejecutar_script"

    md["ad_block"] = ["*"] * num_langs
    md["ad_block"][0] = "ad_block"
    md["ad_block"][1] = "阻止广告"
    md["ad_block"][2] = "blokkeer_advertenties"
    md["ad_block"][3] = "annonces_de_bloc"
    md["ad_block"][4] = "bloccare_gli_annunci"
    md["ad_block"][5] = "ブロック広告"
    md["ad_block"][6] = "광고_차단"
    md["ad_block"][7] = "bloquear_anúncios"
    md["ad_block"][8] = "блокировать_рекламу"
    md["ad_block"][9] = "bloquear_anuncios"

    md["skip"] = ["*"] * num_langs
    md["skip"][0] = "skip"
    md["skip"][1] = "跳过"
    md["skip"][2] = "overslaan"
    md["skip"][3] = "sauter"
    md["skip"][4] = "saltare"
    md["skip"][5] = "スキップ"
    md["skip"][6] = "건너뛸"
    md["skip"][7] = "saltar"
    md["skip"][8] = "пропускать"
    md["skip"][9] = "saltar"

    md["assert_no_404_errors"] = ["*"] * num_langs
    md["assert_no_404_errors"][0] = "assert_no_404_errors"
    md["assert_no_404_errors"][1] = "检查断开的链接"
    md["assert_no_404_errors"][2] = "controleren_op_gebroken_links"
    md["assert_no_404_errors"][3] = "vérifier_les_liens_rompus"
    md["assert_no_404_errors"][4] = "verificare_i_collegamenti"
    md["assert_no_404_errors"][5] = "リンク切れを確認する"
    md["assert_no_404_errors"][6] = "끊어진_링크_확인"
    md["assert_no_404_errors"][7] = "verificar_se_há_links_quebrados"
    md["assert_no_404_errors"][8] = "проверить_ошибки_404"
    md["assert_no_404_errors"][9] = "verificar_si_hay_enlaces_rotos"

    md["assert_no_js_errors"] = ["*"] * num_langs
    md["assert_no_js_errors"][0] = "assert_no_js_errors"
    md["assert_no_js_errors"][1] = "检查JS错误"
    md["assert_no_js_errors"][2] = "controleren_op_js_fouten"
    md["assert_no_js_errors"][3] = "vérifier_les_erreurs_js"
    md["assert_no_js_errors"][4] = "controlla_errori_js"
    md["assert_no_js_errors"][5] = "JSエラーを確認する"
    md["assert_no_js_errors"][6] = "JS_오류_확인"
    md["assert_no_js_errors"][7] = "verificar_se_há_erros_js"
    md["assert_no_js_errors"][8] = "проверить_ошибки_JS"
    md["assert_no_js_errors"][9] = "verificar_si_hay_errores_js"

    md["switch_to_frame"] = ["*"] * num_langs
    md["switch_to_frame"][0] = "switch_to_frame"
    md["switch_to_frame"][1] = "切换到帧"
    md["switch_to_frame"][2] = "overschakelen_naar_frame"
    md["switch_to_frame"][3] = "passer_au_cadre"
    md["switch_to_frame"][4] = "passa_al_frame"
    md["switch_to_frame"][5] = "フレームに切り替え"
    md["switch_to_frame"][6] = "프레임으로_전환"
    md["switch_to_frame"][7] = "mudar_para_o_quadro"
    md["switch_to_frame"][8] = "переключиться_на_кадр"
    md["switch_to_frame"][9] = "cambiar_al_marco"

    md["switch_to_default_content"] = ["*"] * num_langs
    md["switch_to_default_content"][0] = "switch_to_default_content"
    md["switch_to_default_content"][1] = "切换到默认内容"
    md["switch_to_default_content"][2] = "overschakelen_naar_standaardcontent"
    md["switch_to_default_content"][3] = "passer_au_contenu_par_défaut"
    md["switch_to_default_content"][4] = "passa_al_contenuto_predefinito"
    md["switch_to_default_content"][5] = "デフォルトのコンテンツに切り替える"
    md["switch_to_default_content"][6] = "기본_콘텐츠로_전환"
    md["switch_to_default_content"][7] = "mudar_para_o_conteúdo_padrão"
    md["switch_to_default_content"][8] = (
        "переключиться_на_содержимое_по_умолчанию")
    md["switch_to_default_content"][9] = "cambiar_al_contenido_predeterminado"

    md["open_new_window"] = ["*"] * num_langs
    md["open_new_window"][0] = "open_new_window"
    md["open_new_window"][1] = "打开新窗口"
    md["open_new_window"][2] = "nieuw_venster_openen"
    md["open_new_window"][3] = "ouvrir_une_nouvelle_fenêtre"
    md["open_new_window"][4] = "apri_una_nuova_finestra"
    md["open_new_window"][5] = "新しいウィンドウを開く"
    md["open_new_window"][6] = "새_창_열기"
    md["open_new_window"][7] = "abrir_nova_janela"
    md["open_new_window"][8] = "открыть_новое_окно"
    md["open_new_window"][9] = "abrir_una_nueva_ventana"

    md["switch_to_window"] = ["*"] * num_langs
    md["switch_to_window"][0] = "switch_to_window"
    md["switch_to_window"][1] = "切换到窗口"
    md["switch_to_window"][2] = "overschakelen_naar_venster"
    md["switch_to_window"][3] = "passer_à_fenêtre"
    md["switch_to_window"][4] = "passa_alla_finestra"
    md["switch_to_window"][5] = "ウィンドウに切り替え"
    md["switch_to_window"][6] = "창으로_전환"
    md["switch_to_window"][7] = "mudar_para_janela"
    md["switch_to_window"][8] = "переключиться_на_окно"
    md["switch_to_window"][9] = "cambiar_a_ventana"

    md["switch_to_default_window"] = ["*"] * num_langs
    md["switch_to_default_window"][0] = "switch_to_default_window"
    md["switch_to_default_window"][1] = "切换到默认窗口"
    md["switch_to_default_window"][2] = "overschakelen_naar_standaardvenster"
    md["switch_to_default_window"][3] = "passer_à_fenêtre_par_défaut"
    md["switch_to_default_window"][4] = "passa_alla_finestra_predefinita"
    md["switch_to_default_window"][5] = "デフォルトのウィンドウに切り替える"
    md["switch_to_default_window"][6] = "기본_창으로_전환"
    md["switch_to_default_window"][7] = "mudar_para_a_janela_padrão"
    md["switch_to_default_window"][8] = "переключиться_в_окно_по_умолчанию"
    md["switch_to_default_window"][9] = "cambiar_a_ventana_predeterminada"

    md["maximize_window"] = ["*"] * num_langs
    md["maximize_window"][0] = "maximize_window"
    md["maximize_window"][1] = "最大化窗口"
    md["maximize_window"][2] = "venster_maximaliseren"
    md["maximize_window"][3] = "maximiser_fenêtre"
    md["maximize_window"][4] = "ingrandisci_finestra"
    md["maximize_window"][5] = "ウィンドウを最大化する"
    md["maximize_window"][6] = "창_최대화"
    md["maximize_window"][7] = "maximizar_janela"
    md["maximize_window"][8] = "максимальное_окно"
    md["maximize_window"][9] = "maximizar_ventana"

    md["highlight"] = ["*"] * num_langs
    md["highlight"][0] = "highlight"
    md["highlight"][1] = "亮点"
    md["highlight"][2] = "markeren"
    md["highlight"][3] = "illuminer"
    md["highlight"][4] = "illuminare"
    md["highlight"][5] = "ハイライト"
    md["highlight"][6] = "강조"
    md["highlight"][7] = "destaque"
    md["highlight"][8] = "осветить"
    md["highlight"][9] = "resalte"

    md["highlight_click"] = ["*"] * num_langs
    md["highlight_click"][0] = "highlight_click"
    md["highlight_click"][1] = "亮点单击"
    md["highlight_click"][2] = "markeren_klik"
    md["highlight_click"][3] = "illuminer_cliquer"
    md["highlight_click"][4] = "illuminare_clic"
    md["highlight_click"][5] = "ハイライトしてクリックして"
    md["highlight_click"][6] = "강조_클릭"
    md["highlight_click"][7] = "destaque_clique"
    md["highlight_click"][8] = "осветить_нажмите"
    md["highlight_click"][9] = "resalte_clic"

    md["scroll_to"] = ["*"] * num_langs
    md["scroll_to"][0] = "scroll_to"
    md["scroll_to"][1] = "滚动到"
    md["scroll_to"][2] = "scrollen_naar"
    md["scroll_to"][3] = "déménager_à"
    md["scroll_to"][4] = "scorrere_fino_a"
    md["scroll_to"][5] = "スクロールして"
    md["scroll_to"][6] = "요소로_스크롤"
    md["scroll_to"][7] = "rolar_para"
    md["scroll_to"][8] = "прокрутить_к"
    md["scroll_to"][9] = "desplazarse_a"

    md["scroll_to_top"] = ["*"] * num_langs
    md["scroll_to_top"][0] = "scroll_to_top"
    md["scroll_to_top"][1] = "滚动到顶部"
    md["scroll_to_top"][2] = "naar_boven_scrollen"
    md["scroll_to_top"][3] = "faites_défiler_vers_le_haut"
    md["scroll_to_top"][4] = "scorri_verso_alto"
    md["scroll_to_top"][5] = "一番上までスクロール"
    md["scroll_to_top"][6] = "맨_위로_스크롤"
    md["scroll_to_top"][7] = "rolar_para_o_topo"
    md["scroll_to_top"][8] = "пролистать_наверх"
    md["scroll_to_top"][9] = "desplazarse_hasta_la_parte_superior"

    md["scroll_to_bottom"] = ["*"] * num_langs
    md["scroll_to_bottom"][0] = "scroll_to_bottom"
    md["scroll_to_bottom"][1] = "滚动到底部"
    md["scroll_to_bottom"][2] = "naar_beneden_scrollen"
    md["scroll_to_bottom"][3] = "faites_défiler_vers_le_bas"
    md["scroll_to_bottom"][4] = "scorri_verso_il_basso"
    md["scroll_to_bottom"][5] = "一番下までスクロール"
    md["scroll_to_bottom"][6] = "하단으로_스크롤"
    md["scroll_to_bottom"][7] = "rolar_para_o_fundo"
    md["scroll_to_bottom"][8] = "прокрутить_вниз"
    md["scroll_to_bottom"][9] = "desplazarse_hasta_la_parte_inferior"

    md["hover_and_click"] = ["*"] * num_langs
    md["hover_and_click"][0] = "hover_and_click"
    md["hover_and_click"][1] = "悬停并单击"
    md["hover_and_click"][2] = "zweven_en_klik"
    md["hover_and_click"][3] = "planer_au_dessus_et_cliquer"
    md["hover_and_click"][4] = "passa_il_mouse_sopra_e_fai_clic"
    md["hover_and_click"][5] = "上にマウスを移動しクリック"
    md["hover_and_click"][6] = "위로_마우스를_이동하고_클릭"
    md["hover_and_click"][7] = "passe_o_mouse_e_clique"
    md["hover_and_click"][8] = "наведите_и_нажмите"
    md["hover_and_click"][9] = "pasar_el_ratón_y_hacer_clic"

    md["is_selected"] = ["*"] * num_langs
    md["is_selected"][0] = "is_selected"
    md["is_selected"][1] = "是否被选中"
    md["is_selected"][2] = "is_het_geselecteerd"
    md["is_selected"][3] = "est_il_sélectionné"
    md["is_selected"][4] = "è_selezionato"
    md["is_selected"][5] = "選択されていることを"
    md["is_selected"][6] = "선택되어_있는지"
    md["is_selected"][7] = "é_selecionado"
    md["is_selected"][8] = "выбран"
    md["is_selected"][9] = "está_seleccionado"

    md["press_up_arrow"] = ["*"] * num_langs
    md["press_up_arrow"][0] = "press_up_arrow"
    md["press_up_arrow"][1] = "按向上箭头"
    md["press_up_arrow"][2] = "druk_op_pijl_omhoog"
    md["press_up_arrow"][3] = "appuyer_sur_flèche_haut"
    md["press_up_arrow"][4] = "premere_la_freccia_su"
    md["press_up_arrow"][5] = "上矢印を押します"
    md["press_up_arrow"][6] = "위쪽_화살표를_누릅니다"
    md["press_up_arrow"][7] = "pressione_a_seta_para_cima"
    md["press_up_arrow"][8] = "нажмите_стрелку_вверх"
    md["press_up_arrow"][9] = "presione_la_flecha_hacia_arriba"

    md["press_down_arrow"] = ["*"] * num_langs
    md["press_down_arrow"][0] = "press_down_arrow"
    md["press_down_arrow"][1] = "按向下箭头"
    md["press_down_arrow"][2] = "druk_op_pijl_omlaag"
    md["press_down_arrow"][3] = "appuyer_sur_flèche_bas"
    md["press_down_arrow"][4] = "premere_la_freccia_giù"
    md["press_down_arrow"][5] = "下矢印を押します"
    md["press_down_arrow"][6] = "아래쪽_화살표를_누르십시오"
    md["press_down_arrow"][7] = "pressione_a_seta_para_baixo"
    md["press_down_arrow"][8] = "нажмите_стрелку_вниз"
    md["press_down_arrow"][9] = "presione_la_flecha_hacia_abajo"

    md["press_left_arrow"] = ["*"] * num_langs
    md["press_left_arrow"][0] = "press_left_arrow"
    md["press_left_arrow"][1] = "按向左箭头"
    md["press_left_arrow"][2] = "druk_op_pijl_links"
    md["press_left_arrow"][3] = "appuyer_sur_flèche_gauche"
    md["press_left_arrow"][4] = "premere_la_freccia_sinistra"
    md["press_left_arrow"][5] = "左矢印を押します"
    md["press_left_arrow"][6] = "왼쪽_화살표를_누르십시오"
    md["press_left_arrow"][7] = "pressione_a_seta_esquerda"
    md["press_left_arrow"][8] = "нажмите_стрелку_влево"
    md["press_left_arrow"][9] = "presione_la_flecha_izquierda"

    md["press_right_arrow"] = ["*"] * num_langs
    md["press_right_arrow"][0] = "press_right_arrow"
    md["press_right_arrow"][1] = "按向右箭头"
    md["press_right_arrow"][2] = "druk_op_pijl_rechts"
    md["press_right_arrow"][3] = "appuyer_sur_flèche_droite"
    md["press_right_arrow"][4] = "premere_la_freccia_destra"
    md["press_right_arrow"][5] = "右矢印を押します"
    md["press_right_arrow"][6] = "오른쪽_화살표를_누르십시오"
    md["press_right_arrow"][7] = "pressione_a_seta_direita"
    md["press_right_arrow"][8] = "нажмите_стрелку_вправо"
    md["press_right_arrow"][9] = "presione_la_flecha_derecha"

    md["click_visible_elements"] = ["*"] * num_langs
    md["click_visible_elements"][0] = "click_visible_elements"
    md["click_visible_elements"][1] = "单击可见元素"
    md["click_visible_elements"][2] = "klik_zichtbare_elementen"
    md["click_visible_elements"][3] = "cliquer_éléments_visibles"
    md["click_visible_elements"][4] = "fare_clic_sugli_elementi_visibili"
    md["click_visible_elements"][5] = "表示要素をクリックします"
    md["click_visible_elements"][6] = "페이지_요소를_클릭_합니다"
    md["click_visible_elements"][7] = "clique_nos_elementos_visíveis"
    md["click_visible_elements"][8] = "нажмите_видимые_элементы"
    md["click_visible_elements"][9] = "haga_clic_en_elementos_visibles"

    md["select_option_by_text"] = ["*"] * num_langs
    md["select_option_by_text"][0] = "select_option_by_text"
    md["select_option_by_text"][1] = "按文本选择选项"
    md["select_option_by_text"][2] = "optie_selecteren_op_tekst"
    md["select_option_by_text"][3] = "sélectionner_option_par_texte"
    md["select_option_by_text"][4] = "selezionare_opzione_per_testo"
    md["select_option_by_text"][5] = "テキストでオプションを選択"
    md["select_option_by_text"][6] = "텍스트로_옵션_선택"
    md["select_option_by_text"][7] = "selecionar_opção_por_texto"
    md["select_option_by_text"][8] = "выбрать_опцию_по_тексту"
    md["select_option_by_text"][9] = "seleccionar_opción_por_texto"

    md["select_option_by_index"] = ["*"] * num_langs
    md["select_option_by_index"][0] = "select_option_by_index"
    md["select_option_by_index"][1] = "按索引选择选项"
    md["select_option_by_index"][2] = "optie_selecteren_op_index"
    md["select_option_by_index"][3] = "sélectionner_option_par_index"
    md["select_option_by_index"][4] = "selezionare_opzione_per_indice"
    md["select_option_by_index"][5] = "インデックスでオプションを選択"
    md["select_option_by_index"][6] = "인덱스별로_옵션_선택"
    md["select_option_by_index"][7] = "selecionar_opção_por_índice"
    md["select_option_by_index"][8] = "выбрать_опцию_по_индексу"
    md["select_option_by_index"][9] = "seleccionar_opción_por_índice"

    md["select_option_by_value"] = ["*"] * num_langs
    md["select_option_by_value"][0] = "select_option_by_value"
    md["select_option_by_value"][1] = "按值选择选项"
    md["select_option_by_value"][2] = "optie_selecteren_op_waarde"
    md["select_option_by_value"][3] = "sélectionner_option_par_valeur"
    md["select_option_by_value"][4] = "selezionare_opzione_per_valore"
    md["select_option_by_value"][5] = "値でオプションを選択"
    md["select_option_by_value"][6] = "값별로_옵션_선택"
    md["select_option_by_value"][7] = "selecionar_opção_por_valor"
    md["select_option_by_value"][8] = "выбрать_опцию_по_значению"
    md["select_option_by_value"][9] = "seleccionar_opción_por_valor"

    md["create_presentation"] = ["*"] * num_langs
    md["create_presentation"][0] = "create_presentation"
    md["create_presentation"][1] = "创建演示文稿"
    md["create_presentation"][2] = "een_presentatie_maken"
    md["create_presentation"][3] = "créer_une_présentation"
    md["create_presentation"][4] = "creare_una_presentazione"
    md["create_presentation"][5] = "プレゼンテーションを作成する"
    md["create_presentation"][6] = "프레젠테이션_만들기"
    md["create_presentation"][7] = "criar_uma_apresentação"
    md["create_presentation"][8] = "создать_презентацию"
    md["create_presentation"][9] = "crear_una_presentación"

    md["add_slide"] = ["*"] * num_langs
    md["add_slide"][0] = "add_slide"
    md["add_slide"][1] = "添加幻灯片"
    md["add_slide"][2] = "een_dia_toevoegen"
    md["add_slide"][3] = "ajouter_une_diapositive"
    md["add_slide"][4] = "aggiungere_una_diapositiva"
    md["add_slide"][5] = "スライドを追加する"
    md["add_slide"][6] = "슬라이드_추가"
    md["add_slide"][7] = "adicionar_um_slide"
    md["add_slide"][8] = "добавить_слайд"
    md["add_slide"][9] = "añadir_una_diapositiva"

    md["save_presentation"] = ["*"] * num_langs
    md["save_presentation"][0] = "save_presentation"
    md["save_presentation"][1] = "保存演示文稿"
    md["save_presentation"][2] = "de_presentatie_opslaan"
    md["save_presentation"][3] = "enregistrer_la_présentation"
    md["save_presentation"][4] = "salvare_la_presentazione"
    md["save_presentation"][5] = "プレゼンテーションを保存する"
    md["save_presentation"][6] = "프레젠테이션_저장"
    md["save_presentation"][7] = "salvar_a_apresentação"
    md["save_presentation"][8] = "сохранить_презентацию"
    md["save_presentation"][9] = "guardar_la_presentación"

    md["begin_presentation"] = ["*"] * num_langs
    md["begin_presentation"][0] = "begin_presentation"
    md["begin_presentation"][1] = "开始演示文稿"
    md["begin_presentation"][2] = "de_presentatie_starten"
    md["begin_presentation"][3] = "démarrer_la_présentation"
    md["begin_presentation"][4] = "avviare_la_presentazione"
    md["begin_presentation"][5] = "プレゼンテーションを開始する"
    md["begin_presentation"][6] = "프레젠테이션_시작"
    md["begin_presentation"][7] = "iniciar_a_apresentação"
    md["begin_presentation"][8] = "начать_презентацию"
    md["begin_presentation"][9] = "iniciar_la_presentación"

    md["create_tour"] = ["*"] * num_langs
    md["create_tour"][0] = "create_tour"
    md["create_tour"][1] = "创建游览"
    md["create_tour"][2] = "maak_een_tour"
    md["create_tour"][3] = "créer_une_visite"
    md["create_tour"][4] = "creare_un_tour"
    md["create_tour"][5] = "ツアーを作成する"
    md["create_tour"][6] = "가이드_투어_만들기"
    md["create_tour"][7] = "criar_um_tour"
    md["create_tour"][8] = "создать_тур"
    md["create_tour"][9] = "crear_una_gira"

    md["create_shepherd_tour"] = ["*"] * num_langs
    md["create_shepherd_tour"][0] = "create_shepherd_tour"
    md["create_shepherd_tour"][1] = "创建SHEPHERD游览"
    md["create_shepherd_tour"][2] = "maak_een_shepherd_tour"
    md["create_shepherd_tour"][3] = "créer_une_visite_shepherd"
    md["create_shepherd_tour"][4] = "creare_un_tour_shepherd"
    md["create_shepherd_tour"][5] = "SHEPHERDツアーを作成する"
    md["create_shepherd_tour"][6] = "가이드_SHEPHERD_투어_만들기"
    md["create_shepherd_tour"][7] = "criar_um_tour_shepherd"
    md["create_shepherd_tour"][8] = "создать_SHEPHERD_тур"
    md["create_shepherd_tour"][9] = "crear_una_gira_shepherd"

    md["create_bootstrap_tour"] = ["*"] * num_langs
    md["create_bootstrap_tour"][0] = "create_bootstrap_tour"
    md["create_bootstrap_tour"][1] = "创建BOOTSTRAP游览"
    md["create_bootstrap_tour"][2] = "maak_een_bootstrap_tour"
    md["create_bootstrap_tour"][3] = "créer_une_visite_bootstrap"
    md["create_bootstrap_tour"][4] = "creare_un_tour_bootstrap"
    md["create_bootstrap_tour"][5] = "BOOTSTRAPツアーを作成する"
    md["create_bootstrap_tour"][6] = "가이드_BOOTSTRAP_투어_만들기"
    md["create_bootstrap_tour"][7] = "criar_um_tour_bootstrap"
    md["create_bootstrap_tour"][8] = "создать_BOOTSTRAP_тур"
    md["create_bootstrap_tour"][9] = "crear_una_gira_bootstrap"

    md["create_driverjs_tour"] = ["*"] * num_langs
    md["create_driverjs_tour"][0] = "create_driverjs_tour"
    md["create_driverjs_tour"][1] = "创建DRIVERJS游览"
    md["create_driverjs_tour"][2] = "maak_een_driverjs_tour"
    md["create_driverjs_tour"][3] = "créer_une_visite_driverjs"
    md["create_driverjs_tour"][4] = "creare_un_tour_driverjs"
    md["create_driverjs_tour"][5] = "DRIVERJSツアーを作成する"
    md["create_driverjs_tour"][6] = "가이드_DRIVERJS_투어_만들기"
    md["create_driverjs_tour"][7] = "criar_um_tour_driverjs"
    md["create_driverjs_tour"][8] = "создать_DRIVERJS_тур"
    md["create_driverjs_tour"][9] = "crear_una_gira_driverjs"

    md["create_hopscotch_tour"] = ["*"] * num_langs
    md["create_hopscotch_tour"][0] = "create_hopscotch_tour"
    md["create_hopscotch_tour"][1] = "创建HOPSCOTCH游览"
    md["create_hopscotch_tour"][2] = "maak_een_hopscotch_tour"
    md["create_hopscotch_tour"][3] = "créer_une_visite_hopscotch"
    md["create_hopscotch_tour"][4] = "creare_un_tour_hopscotch"
    md["create_hopscotch_tour"][5] = "HOPSCOTCHツアーを作成する"
    md["create_hopscotch_tour"][6] = "가이드_HOPSCOTCH_투어_만들기"
    md["create_hopscotch_tour"][7] = "criar_um_tour_hopscotch"
    md["create_hopscotch_tour"][8] = "создать_HOPSCOTCH_тур"
    md["create_hopscotch_tour"][9] = "crear_una_gira_hopscotch"

    md["create_introjs_tour"] = ["*"] * num_langs
    md["create_introjs_tour"][0] = "create_introjs_tour"
    md["create_introjs_tour"][1] = "创建INTROJS游览"
    md["create_introjs_tour"][2] = "maak_een_introjs_tour"
    md["create_introjs_tour"][3] = "créer_une_visite_introjs"
    md["create_introjs_tour"][4] = "creare_un_tour_introjs"
    md["create_introjs_tour"][5] = "INTROJSツアーを作成する"
    md["create_introjs_tour"][6] = "가이드_INTROJS_투어_만들기"
    md["create_introjs_tour"][7] = "criar_um_tour_introjs"
    md["create_introjs_tour"][8] = "создать_INTROJS_тур"
    md["create_introjs_tour"][9] = "crear_una_gira_introjs"

    md["add_tour_step"] = ["*"] * num_langs
    md["add_tour_step"][0] = "add_tour_step"
    md["add_tour_step"][1] = "添加游览步骤"
    md["add_tour_step"][2] = "toevoegen_tour_stap"
    md["add_tour_step"][3] = "ajouter_étape_à_la_visite"
    md["add_tour_step"][4] = "aggiungere_passo_al_tour"
    md["add_tour_step"][5] = "ツアーステップを追加する"
    md["add_tour_step"][6] = "둘러보기_단계_추가"
    md["add_tour_step"][7] = "adicionar_passo_para_o_tour"
    md["add_tour_step"][8] = "добавить_шаг_в_тур"
    md["add_tour_step"][9] = "agregar_paso_a_la_gira"

    md["play_tour"] = ["*"] * num_langs
    md["play_tour"][0] = "play_tour"
    md["play_tour"][1] = "播放游览"
    md["play_tour"][2] = "speel_de_tour"
    md["play_tour"][3] = "jouer_la_visite"
    md["play_tour"][4] = "riprodurre_il_tour"
    md["play_tour"][5] = "ツアーを再生する"
    md["play_tour"][6] = "가이드_투어를하다"
    md["play_tour"][7] = "jogar_o_tour"
    md["play_tour"][8] = "играть_тур"
    md["play_tour"][9] = "reproducir_la_gira"

    md["export_tour"] = ["*"] * num_langs
    md["export_tour"][0] = "export_tour"
    md["export_tour"][1] = "导出游览"
    md["export_tour"][2] = "de_tour_exporteren"
    md["export_tour"][3] = "exporter_la_visite"
    md["export_tour"][4] = "esportare_il_tour"
    md["export_tour"][5] = "ツアーをエクスポートする"
    md["export_tour"][6] = "가이드_투어_내보내기"
    md["export_tour"][7] = "exportar_o_tour"
    md["export_tour"][8] = "экспортировать_тур"
    md["export_tour"][9] = "exportar_la_gira"

    md["fail"] = ["*"] * num_langs
    md["fail"][0] = "fail"
    md["fail"][1] = "失败"
    md["fail"][2] = "mislukken"
    md["fail"][3] = "échouer"
    md["fail"][4] = "fallire"
    md["fail"][5] = "失敗"
    md["fail"][6] = "실패"
    md["fail"][7] = "falhar"
    md["fail"][8] = "провалить"
    md["fail"][9] = "fallar"

    md["get"] = ["*"] * num_langs
    md["get"][0] = "get"
    md["get"][1] = "获取"
    md["get"][2] = "ophalen"
    md["get"][3] = "obtenir"
    md["get"][4] = "ottenere"
    md["get"][5] = "を取得する"
    md["get"][6] = "받기"
    md["get"][7] = "obter"
    md["get"][8] = "получить"
    md["get"][9] = "obtener"

    md["visit"] = ["*"] * num_langs
    md["visit"][0] = "visit"
    md["visit"][1] = "访问"
    md["visit"][2] = "bezoek"
    md["visit"][3] = "visiter"
    md["visit"][4] = "visita"
    md["visit"][5] = "を訪問"
    md["visit"][6] = "방문"
    md["visit"][7] = "visitar"
    md["visit"][8] = "посетить"
    md["visit"][9] = "visita"

    md["visit_url"] = ["*"] * num_langs
    md["visit_url"][0] = "visit_url"
    md["visit_url"][1] = "访问网址"
    md["visit_url"][2] = "bezoek_url"
    md["visit_url"][3] = "visiter_url"
    md["visit_url"][4] = "visita_url"
    md["visit_url"][5] = "URLを訪問"
    md["visit_url"][6] = "방문_URL"
    md["visit_url"][7] = "visitar_url"
    md["visit_url"][8] = "посетить_URL"
    md["visit_url"][9] = "visita_url"

    md["get_element"] = ["*"] * num_langs
    md["get_element"][0] = "get_element"
    md["get_element"][1] = "获取元素"
    md["get_element"][2] = "element_ophalen"
    md["get_element"][3] = "obtenir_élément"
    md["get_element"][4] = "ottenere_elemento"
    md["get_element"][5] = "要素を取得する"
    md["get_element"][6] = "요소_검색"
    md["get_element"][7] = "obter_elemento"
    md["get_element"][8] = "получить_элемент"
    md["get_element"][9] = "obtener_elemento"

    md["find_element"] = ["*"] * num_langs
    md["find_element"][0] = "find_element"
    md["find_element"][1] = "查找元素"
    md["find_element"][2] = "vind_element"
    md["find_element"][3] = "trouver_élément"
    md["find_element"][4] = "trovare_elemento"
    md["find_element"][5] = "要素を見つける"
    md["find_element"][6] = "요소를_찾을"
    md["find_element"][7] = "encontrar_elemento"
    md["find_element"][8] = "найти_элемент"
    md["find_element"][9] = "encontrar_elemento"

    md["find_text"] = ["*"] * num_langs
    md["find_text"][0] = "find_text"
    md["find_text"][1] = "查找文本"
    md["find_text"][2] = "vind_tekst"
    md["find_text"][3] = "trouver_texte"
    md["find_text"][4] = "trovare_testo"
    md["find_text"][5] = "テキストを見つける"
    md["find_text"][6] = "텍스트_찾기"
    md["find_text"][7] = "encontrar_texto"
    md["find_text"][8] = "найти_текст"
    md["find_text"][9] = "encontrar_texto"

    md["get_attribute"] = ["*"] * num_langs
    md["get_attribute"][0] = "get_attribute"
    md["get_attribute"][1] = "获取属性"
    md["get_attribute"][2] = "kenmerk_ophalen"
    md["get_attribute"][3] = "obtenir_attribut"
    md["get_attribute"][4] = "ottenere_attributo"
    md["get_attribute"][5] = "属性を取得する"
    md["get_attribute"][6] = "특성_검색"
    md["get_attribute"][7] = "obter_atributo"
    md["get_attribute"][8] = "получить_атрибут"
    md["get_attribute"][9] = "obtener_atributo"

    md["set_attribute"] = ["*"] * num_langs
    md["set_attribute"][0] = "set_attribute"
    md["set_attribute"][1] = "设置属性"
    md["set_attribute"][2] = "kenmerk_instellen"
    md["set_attribute"][3] = "définir_attribut"
    md["set_attribute"][4] = "imposta_attributo"
    md["set_attribute"][5] = "属性を設定する"
    md["set_attribute"][6] = "특성_설정"
    md["set_attribute"][7] = "definir_atributo"
    md["set_attribute"][8] = "набор_атрибута"
    md["set_attribute"][9] = "establecer_atributo"

    md["set_attributes"] = ["*"] * num_langs
    md["set_attributes"][0] = "set_attributes"
    md["set_attributes"][1] = "设置所有属性"
    md["set_attributes"][2] = "kenmerken_instellen"
    md["set_attributes"][3] = "définir_attributs"
    md["set_attributes"][4] = "impostare_gli_attributi"
    md["set_attributes"][5] = "すべての属性を設定"
    md["set_attributes"][6] = "모든_특성_설정"
    md["set_attributes"][7] = "definir_atributos"
    md["set_attributes"][8] = "набор_атрибутов"
    md["set_attributes"][9] = "establecer_atributos"

    md["type"] = ["*"] * num_langs
    md["type"][0] = "type"
    md["type"][1] = "输入文本"
    md["type"][2] = "typ"
    md["type"][3] = "taper"
    md["type"][4] = "digitare"
    md["type"][5] = "入力"
    md["type"][6] = "입력"
    md["type"][7] = "tipo"
    md["type"][8] = "введите"
    md["type"][9] = "escriba"

    md["write"] = ["*"] * num_langs
    md["write"][0] = "write"
    md["write"][1] = "写文本"
    md["write"][2] = "schrijven"
    md["write"][3] = "écriver"
    md["write"][4] = "scrivere"
    md["write"][5] = "書く"
    md["write"][6] = "쓰다"
    md["write"][7] = "escreva"
    md["write"][8] = "написать"
    md["write"][9] = "escribir"

    md["set_messenger_theme"] = ["*"] * num_langs
    md["set_messenger_theme"][0] = "set_messenger_theme"
    md["set_messenger_theme"][1] = "设置消息主题"
    md["set_messenger_theme"][2] = "kenmerk_thema_van_bericht"
    md["set_messenger_theme"][3] = "définir_thème_du_message"
    md["set_messenger_theme"][4] = "impostare_tema_del_messaggio"
    md["set_messenger_theme"][5] = "メッセージのスタイルを設定する"
    md["set_messenger_theme"][6] = "메시지_테마_설정"
    md["set_messenger_theme"][7] = "definir_tema_da_mensagem"
    md["set_messenger_theme"][8] = "набор_тему_сообщения"
    md["set_messenger_theme"][9] = "establecer_tema_del_mensaje"

    md["post_message"] = ["*"] * num_langs
    md["post_message"][0] = "post_message"
    md["post_message"][1] = "显示讯息"
    md["post_message"][2] = "bericht_weergeven"
    md["post_message"][3] = "afficher_message"
    md["post_message"][4] = "visualizza_messaggio"
    md["post_message"][5] = "メッセージを表示する"
    md["post_message"][6] = "메시지를_표시"
    md["post_message"][7] = "exibir_mensagem"
    md["post_message"][8] = "показать_сообщение"
    md["post_message"][9] = "mostrar_mensaje"

    md["_print"] = ["*"] * num_langs
    md["_print"][0] = "_print"
    md["_print"][1] = "打印"
    md["_print"][2] = "afdrukken"
    md["_print"][3] = "imprimer"
    md["_print"][4] = "stampare"
    md["_print"][5] = "印刷"
    md["_print"][6] = "인쇄"
    md["_print"][7] = "imprimir"
    md["_print"][8] = "печатать"
    md["_print"][9] = "imprimir"

    md["deferred_assert_element"] = ["*"] * num_langs
    md["deferred_assert_element"][0] = "deferred_assert_element"
    md["deferred_assert_element"][1] = "推迟断言元素"
    md["deferred_assert_element"][2] = "uitgestelde_controleren_element"
    md["deferred_assert_element"][3] = "reporté_vérifier_élément"
    md["deferred_assert_element"][4] = "differita_verificare_elemento"
    md["deferred_assert_element"][5] = "を延期する要素を確認する"
    md["deferred_assert_element"][6] = "연기된_요소_확인"
    md["deferred_assert_element"][7] = "adiada_verificar_elemento"
    md["deferred_assert_element"][8] = "отложенный_подтвердить_элемент"
    md["deferred_assert_element"][9] = "diferido_verificar_elemento"

    md["deferred_assert_text"] = ["*"] * num_langs
    md["deferred_assert_text"][0] = "deferred_assert_text"
    md["deferred_assert_text"][1] = "推迟断言文本"
    md["deferred_assert_text"][2] = "uitgestelde_controleren_tekst"
    md["deferred_assert_text"][3] = "reporté_vérifier_texte"
    md["deferred_assert_text"][4] = "differita_verificare_testo"
    md["deferred_assert_text"][5] = "を延期するテキストを確認する"
    md["deferred_assert_text"][6] = "연기된_텍스트_확인"
    md["deferred_assert_text"][7] = "adiada_verificar_texto"
    md["deferred_assert_text"][8] = "отложенный_подтвердить_текст"
    md["deferred_assert_text"][9] = "diferido_verificar_texto"

    md["process_deferred_asserts"] = ["*"] * num_langs
    md["process_deferred_asserts"][0] = "process_deferred_asserts"
    md["process_deferred_asserts"][1] = "处理推迟断言"
    md["process_deferred_asserts"][2] = "verwerken_uitgestelde_controleren"
    md["process_deferred_asserts"][3] = "effectuer_vérifications_reportées"
    md["process_deferred_asserts"][4] = "elaborare_differita_verificari"
    md["process_deferred_asserts"][5] = "遅延アサーションの処理"
    md["process_deferred_asserts"][6] = "연기된_검증_처리"
    md["process_deferred_asserts"][7] = "processar_verificações_adiada"
    md["process_deferred_asserts"][8] = "обработки_отложенных_подтверждений"
    md["process_deferred_asserts"][9] = "procesar_verificaciones_diferidas"

    md["accept_alert"] = ["*"] * num_langs
    md["accept_alert"][0] = "accept_alert"
    md["accept_alert"][1] = "接受警报"
    md["accept_alert"][2] = "waarschuwing_accepteren"
    md["accept_alert"][3] = "accepter_alerte"
    md["accept_alert"][4] = "accetta_avviso"
    md["accept_alert"][5] = "アラートを受け入れる"
    md["accept_alert"][6] = "경고를_수락"
    md["accept_alert"][7] = "aceitar_alerta"
    md["accept_alert"][8] = "принять_оповещение"
    md["accept_alert"][9] = "aceptar_alerta"

    md["dismiss_alert"] = ["*"] * num_langs
    md["dismiss_alert"][0] = "dismiss_alert"
    md["dismiss_alert"][1] = "解除警报"
    md["dismiss_alert"][2] = "waarschuwing_wegsturen"
    md["dismiss_alert"][3] = "rejeter_alerte"
    md["dismiss_alert"][4] = "elimina_avviso"
    md["dismiss_alert"][5] = "アラートを却下"
    md["dismiss_alert"][6] = "경고를_거부"
    md["dismiss_alert"][7] = "demitir_alerta"
    md["dismiss_alert"][8] = "увольнять_оповещение"
    md["dismiss_alert"][9] = "descartar_alerta"

    md["switch_to_alert"] = ["*"] * num_langs
    md["switch_to_alert"][0] = "switch_to_alert"
    md["switch_to_alert"][1] = "切换到警报"
    md["switch_to_alert"][2] = "overschakelen_naar_waarschuwing"
    md["switch_to_alert"][3] = "passer_à_alerte"
    md["switch_to_alert"][4] = "passa_al_avviso"
    md["switch_to_alert"][5] = "アラートに切り替え"
    md["switch_to_alert"][6] = "경고로_전환"
    md["switch_to_alert"][7] = "mudar_para_alerta"
    md["switch_to_alert"][8] = "переключиться_на_оповещение"
    md["switch_to_alert"][9] = "cambiar_a_alerta"

    md["load_html_file"] = ["*"] * num_langs
    md["load_html_file"][0] = "load_html_file"
    md["load_html_file"][1] = "加载HTML文件"
    md["load_html_file"][2] = "html_bestand_laden"
    md["load_html_file"][3] = "charger_html_fichier"
    md["load_html_file"][4] = "caricare_html_file"
    md["load_html_file"][5] = "HTMLファイルを読み込む"
    md["load_html_file"][6] = "HTML_파일_로드"
    md["load_html_file"][7] = "carregar_arquivo_html"
    md["load_html_file"][8] = "загрузить_HTML_файл"
    md["load_html_file"][9] = "cargar_archivo_html"

    md["open_html_file"] = ["*"] * num_langs
    md["open_html_file"][0] = "open_html_file"
    md["open_html_file"][1] = "打开HTML文件"
    md["open_html_file"][2] = "html_bestand_openen"
    md["open_html_file"][3] = "ouvrir_html_fichier"
    md["open_html_file"][4] = "apri_html_file"
    md["open_html_file"][5] = "HTMLファイルを開く"
    md["open_html_file"][6] = "HTML_파일_열기"
    md["open_html_file"][7] = "abrir_arquivo_html"
    md["open_html_file"][8] = "открыть_HTML_файл"
    md["open_html_file"][9] = "abrir_archivo_html"

    md["get_user_agent"] = ["*"] * num_langs
    md["get_user_agent"][0] = "get_user_agent"
    md["get_user_agent"][1] = "获取用户代理"
    md["get_user_agent"][2] = "gebruikersagent_ophalen"
    md["get_user_agent"][3] = "obtenir_agent_utilisateur"
    md["get_user_agent"][4] = "ottenere_agente_utente"
    md["get_user_agent"][5] = "ユーザーエージェントの取得"
    md["get_user_agent"][6] = "사용자_에이전트_가져_오기"
    md["get_user_agent"][7] = "obter_agente_do_usuário"
    md["get_user_agent"][8] = "получить_агента_пользователя"
    md["get_user_agent"][9] = "obtener_agente_de_usuario"

    ################
    # Duplicates

    # "input" -> duplicate of "type"
    md["input"] = ["*"] * num_langs
    md["input"][0] = "input"
    md["input"][1] = "输入文本"
    md["input"][2] = "typ"
    md["input"][3] = "taper"
    md["input"][4] = "digitare"
    md["input"][5] = "入力"
    md["input"][6] = "입력"
    md["input"][7] = "tipo"
    md["input"][8] = "введите"
    md["input"][9] = "escriba"

    # "goto" -> duplicate of "visit"
    md["goto"] = ["*"] * num_langs
    md["goto"][0] = "goto"
    md["goto"][1] = "访问"
    md["goto"][2] = "bezoek"
    md["goto"][3] = "visiter"
    md["goto"][4] = "visita"
    md["goto"][5] = "を訪問"
    md["goto"][6] = "방문"
    md["goto"][7] = "visitar"
    md["goto"][8] = "посетить"
    md["goto"][9] = "visita"

    # "go_to" -> duplicate of "visit"
    md["go_to"] = ["*"] * num_langs
    md["go_to"][0] = "go_to"
    md["go_to"][1] = "访问"
    md["go_to"][2] = "bezoek"
    md["go_to"][3] = "visiter"
    md["go_to"][4] = "visita"
    md["go_to"][5] = "を訪問"
    md["go_to"][6] = "방문"
    md["go_to"][7] = "visitar"
    md["go_to"][8] = "посетить"
    md["go_to"][9] = "visita"

    # "refresh" -> duplicate of "refresh_page"
    md["refresh"] = ["*"] * num_langs
    md["refresh"][0] = "refresh"
    md["refresh"][1] = "刷新页面"
    md["refresh"][2] = "ververs_pagina"
    md["refresh"][3] = "rafraîchir_la_page"
    md["refresh"][4] = "aggiorna_la_pagina"
    md["refresh"][5] = "ページを更新する"
    md["refresh"][6] = "페이지_새로_고침"
    md["refresh"][7] = "atualizar_a_página"
    md["refresh"][8] = "обновить_страницу"
    md["refresh"][9] = "actualizar_la_página"

    # "reload" -> duplicate of "refresh_page"
    md["reload"] = ["*"] * num_langs
    md["reload"][0] = "reload"
    md["reload"][1] = "刷新页面"
    md["reload"][2] = "ververs_pagina"
    md["reload"][3] = "rafraîchir_la_page"
    md["reload"][4] = "aggiorna_la_pagina"
    md["reload"][5] = "ページを更新する"
    md["reload"][6] = "페이지_새로_고침"
    md["reload"][7] = "atualizar_a_página"
    md["reload"][8] = "обновить_страницу"
    md["reload"][9] = "actualizar_la_página"

    # "reload_page" -> duplicate of "refresh_page"
    md["reload_page"] = ["*"] * num_langs
    md["reload_page"][0] = "reload_page"
    md["reload_page"][1] = "刷新页面"
    md["reload_page"][2] = "ververs_pagina"
    md["reload_page"][3] = "rafraîchir_la_page"
    md["reload_page"][4] = "aggiorna_la_pagina"
    md["reload_page"][5] = "ページを更新する"
    md["reload_page"][6] = "페이지_새로_고침"
    md["reload_page"][7] = "atualizar_a_página"
    md["reload_page"][8] = "обновить_страницу"
    md["reload_page"][9] = "actualizar_la_página"

    # "get_page_title" -> duplicate of "get_title"
    md["get_page_title"] = ["*"] * num_langs
    md["get_page_title"][0] = "get_page_title"
    md["get_page_title"][1] = "获取标题"
    md["get_page_title"][2] = "titel_ophalen"
    md["get_page_title"][3] = "obtenir_le_titre"
    md["get_page_title"][4] = "ottenere_il_titolo"
    md["get_page_title"][5] = "タイトルを取得する"
    md["get_page_title"][6] = "제목_검색"
    md["get_page_title"][7] = "obter_título"
    md["get_page_title"][8] = "получить_название"
    md["get_page_title"][9] = "obtener_título"

    # "click_link" -> duplicate of "click_link_text"
    md["click_link"] = ["*"] * num_langs
    md["click_link"][0] = "click_link"
    md["click_link"][1] = "单击链接文本"
    md["click_link"][2] = "klik_linktekst"
    md["click_link"][3] = "cliquer_texte_du_lien"
    md["click_link"][4] = "fare_clic_testo_del_collegamento"
    md["click_link"][5] = "リンクテキストをクリックします"
    md["click_link"][6] = "링크_텍스트를_클릭합니다"
    md["click_link"][7] = "clique_texto_do_link"
    md["click_link"][8] = "нажмите_ссылку"
    md["click_link"][9] = "haga_clic_texto_del_enlace"

    # "send_keys" -> duplicate of "add_text"
    md["send_keys"] = ["*"] * num_langs
    md["send_keys"][0] = "send_keys"
    md["send_keys"][1] = "添加文本"
    md["send_keys"][2] = "tekst_toevoegen"
    md["send_keys"][3] = "ajouter_texte"
    md["send_keys"][4] = "aggiungi_testo"
    md["send_keys"][5] = "テキストを追加"
    md["send_keys"][6] = "텍스트를_추가"
    md["send_keys"][7] = "adicionar_texto"
    md["send_keys"][8] = "добавить_текст"
    md["send_keys"][9] = "agregar_texto"

    # "set_attribute_all" -> duplicate of "set_attributes"
    md["set_attribute_all"] = ["*"] * num_langs
    md["set_attribute_all"][0] = "set_attribute_all"
    md["set_attribute_all"][1] = "设置所有属性"
    md["set_attribute_all"][2] = "kenmerken_instellen"
    md["set_attribute_all"][3] = "définir_attributs"
    md["set_attribute_all"][4] = "impostare_gli_attributi"
    md["set_attribute_all"][5] = "すべての属性を設定"
    md["set_attribute_all"][6] = "모든_특성_설정"
    md["set_attribute_all"][7] = "definir_atributos"
    md["set_attribute_all"][8] = "набор_атрибутов"
    md["set_attribute_all"][9] = "establecer_atributos"

    # "is_checked" -> duplicate of "is_selected"
    md["is_checked"] = ["*"] * num_langs
    md["is_checked"][0] = "is_checked"
    md["is_checked"][1] = "是否被选中"
    md["is_checked"][2] = "is_het_geselecteerd"
    md["is_checked"][3] = "est_il_sélectionné"
    md["is_checked"][4] = "è_selezionato"
    md["is_checked"][5] = "選択されていることを"
    md["is_checked"][6] = "선택되어_있는지"
    md["is_checked"][7] = "é_selecionado"
    md["is_checked"][8] = "выбран"
    md["is_checked"][9] = "está_seleccionado"

    # "wait_for_text_visible" -> duplicate of "wait_for_text"
    md["wait_for_text_visible"] = ["*"] * num_langs
    md["wait_for_text_visible"][0] = "wait_for_text_visible"
    md["wait_for_text_visible"][1] = "等待文本"
    md["wait_for_text_visible"][2] = "wachten_op_tekst"
    md["wait_for_text_visible"][3] = "attendre_le_texte"
    md["wait_for_text_visible"][4] = "attendere_il_testo"
    md["wait_for_text_visible"][5] = "テキストを待つ"
    md["wait_for_text_visible"][6] = "텍스트가_나타날_때까지_기다립니다"
    md["wait_for_text_visible"][7] = "aguardar_o_texto"
    md["wait_for_text_visible"][8] = "ждать_текста"
    md["wait_for_text_visible"][9] = "espera_el_texto"

    # "assert_text_visible" -> duplicate of "assert_text"
    md["assert_text_visible"] = ["*"] * num_langs
    md["assert_text_visible"][0] = "assert_text_visible"
    md["assert_text_visible"][1] = "断言文本"
    md["assert_text_visible"][2] = "controleren_tekst"
    md["assert_text_visible"][3] = "vérifier_texte"
    md["assert_text_visible"][4] = "verificare_testo"
    md["assert_text_visible"][5] = "テキストを確認する"
    md["assert_text_visible"][6] = "텍스트_확인"
    md["assert_text_visible"][7] = "verificar_texto"
    md["assert_text_visible"][8] = "подтвердить_текст"
    md["assert_text_visible"][9] = "verificar_texto"

    # "assert_no_broken_links" -> duplicate of "assert_no_404_errors"
    md["assert_no_broken_links"] = ["*"] * num_langs
    md["assert_no_broken_links"][0] = "assert_no_broken_links"
    md["assert_no_broken_links"][1] = "检查断开的链接"
    md["assert_no_broken_links"][2] = "controleren_op_gebroken_links"
    md["assert_no_broken_links"][3] = "vérifier_les_liens_rompus"
    md["assert_no_broken_links"][4] = "verificare_i_collegamenti"
    md["assert_no_broken_links"][5] = "リンク切れを確認する"
    md["assert_no_broken_links"][6] = "끊어진_링크_확인"
    md["assert_no_broken_links"][7] = "verificar_se_há_links_quebrados"
    md["assert_no_broken_links"][8] = "проверить_ошибки_404"
    md["assert_no_broken_links"][9] = "verificar_si_hay_enlaces_rotos"

    # "block_ads" -> duplicate of "ad_block"
    md["block_ads"] = ["*"] * num_langs
    md["block_ads"][0] = "block_ads"
    md["block_ads"][1] = "阻止广告"
    md["block_ads"][2] = "blokkeer_advertenties"
    md["block_ads"][3] = "annonces_de_bloc"
    md["block_ads"][4] = "bloccare_gli_annunci"
    md["block_ads"][5] = "ブロック広告"
    md["block_ads"][6] = "광고_차단"
    md["block_ads"][7] = "bloquear_anúncios"
    md["block_ads"][8] = "блокировать_рекламу"
    md["block_ads"][9] = "bloquear_anuncios"

    # "start_tour" -> duplicate of "play_tour"
    md["start_tour"] = ["*"] * num_langs
    md["start_tour"][0] = "start_tour"
    md["start_tour"][1] = "播放游览"
    md["start_tour"][2] = "speel_de_tour"
    md["start_tour"][3] = "jouer_la_visite"
    md["start_tour"][4] = "riprodurre_il_tour"
    md["start_tour"][5] = "ツアーを再生する"
    md["start_tour"][6] = "가이드_투어를하다"
    md["start_tour"][7] = "jogar_o_tour"
    md["start_tour"][8] = "играть_тур"
    md["start_tour"][9] = "reproducir_la_gira"

    # "wait_for_and_accept_alert" -> duplicate of "accept_alert"
    md["wait_for_and_accept_alert"] = ["*"] * num_langs
    md["wait_for_and_accept_alert"][0] = "wait_for_and_accept_alert"
    md["wait_for_and_accept_alert"][1] = "接受警报"
    md["wait_for_and_accept_alert"][2] = "waarschuwing_accepteren"
    md["wait_for_and_accept_alert"][3] = "accepter_alerte"
    md["wait_for_and_accept_alert"][4] = "accetta_avviso"
    md["wait_for_and_accept_alert"][5] = "アラートを受け入れる"
    md["wait_for_and_accept_alert"][6] = "경고를_수락"
    md["wait_for_and_accept_alert"][7] = "aceitar_alerta"
    md["wait_for_and_accept_alert"][8] = "принять_оповещение"
    md["wait_for_and_accept_alert"][9] = "aceptar_alerta"

    # "wait_for_and_dismiss_alert" -> duplicate of "dismiss_alert"
    md["wait_for_and_dismiss_alert"] = ["*"] * num_langs
    md["wait_for_and_dismiss_alert"][0] = "wait_for_and_dismiss_alert"
    md["wait_for_and_dismiss_alert"][1] = "解除警报"
    md["wait_for_and_dismiss_alert"][2] = "waarschuwing_wegsturen"
    md["wait_for_and_dismiss_alert"][3] = "rejeter_alerte"
    md["wait_for_and_dismiss_alert"][4] = "elimina_avviso"
    md["wait_for_and_dismiss_alert"][5] = "アラートを却下"
    md["wait_for_and_dismiss_alert"][6] = "경고를_거부"
    md["wait_for_and_dismiss_alert"][7] = "demitir_alerta"
    md["wait_for_and_dismiss_alert"][8] = "увольнять_оповещение"
    md["wait_for_and_dismiss_alert"][9] = "descartar_alerta"

    # "wait_for_and_switch_to_alert" -> duplicate of "switch_to_alert"
    md["wait_for_and_switch_to_alert"] = ["*"] * num_langs
    md["wait_for_and_switch_to_alert"][0] = "wait_for_and_switch_to_alert"
    md["wait_for_and_switch_to_alert"][1] = "切换到警报"
    md["wait_for_and_switch_to_alert"][2] = "overschakelen_naar_waarschuwing"
    md["wait_for_and_switch_to_alert"][3] = "passer_à_alerte"
    md["wait_for_and_switch_to_alert"][4] = "passa_al_avviso"
    md["wait_for_and_switch_to_alert"][5] = "アラートに切り替え"
    md["wait_for_and_switch_to_alert"][6] = "경고로_전환"
    md["wait_for_and_switch_to_alert"][7] = "mudar_para_alerta"
    md["wait_for_and_switch_to_alert"][8] = "переключиться_на_оповещение"
    md["wait_for_and_switch_to_alert"][9] = "cambiar_a_alerta"

    ################
    # MasterQA Only!

    md["verify"] = ["*"] * num_langs
    md["verify"][0] = "verify"
    md["verify"][1] = "校验"
    md["verify"][2] = "controleren"
    md["verify"][3] = "vérifier"
    md["verify"][4] = "verificare"
    md["verify"][5] = "を確認する"
    md["verify"][6] = "확인"
    md["verify"][7] = "verificar"
    md["verify"][8] = "подтвердить"
    md["verify"][9] = "verificar"
