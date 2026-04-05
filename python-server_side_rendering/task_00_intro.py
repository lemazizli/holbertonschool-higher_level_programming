import os

def generate_invitations(template, attendees):
    # 1. Giriş Tiplərinin Yoxlanılması
    if not isinstance(template, str):
        print(f"Səhv: Şablon sətir (string) tipində olmalıdır. Alınan tip: {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Səhv: İştirakçılar siyahı (list of dictionaries) tipində olmalıdır.")
        return

    # 2. Boş Girişlərin Yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Hər bir İştirakçının Emal Edilməsi
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        # Əvəzlənəcək sahələrin siyahısı
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            # Məlumatı götürürük, əgər yoxdursa və ya None-dırsa "N/A" istifadə edirik
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            # Şablondakı {key} hissəsini real məlumatla əvəz edirik
            processed_template = processed_template.replace(f"{{{key}}}", str(value))

        # 4. Çıxış Fayllarının Yaradılması
        file_name = f"output_{index}.txt"
        # Əgər fayl artıq mövcuddursa üzərinə yazılacaq
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Fayl yazılarkən xəta baş verdi {file_name}: {e}")import os

def generate_invitations(template, attendees):
    # 1. Giriş Tiplərinin Yoxlanılması
    if not isinstance(template, str):
        print(f"Səhv: Şablon sətir (string) tipində olmalıdır. Alınan tip: {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Səhv: İştirakçılar siyahı (list of dictionaries) tipində olmalıdır.")
        return

    # 2. Boş Girişlərin Yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Hər bir İştirakçının Emal Edilməsi
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        # Əvəzlənəcək sahələrin siyahısı
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            # Məlumatı götürürük, əgər yoxdursa və ya None-dırsa "N/A" istifadə edirik
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            # Şablondakı {key} hissəsini real məlumatla əvəz edirik
            processed_template = processed_template.replace(f"{{{key}}}", str(value))

        # 4. Çıxış Fayllarının Yaradılması
        file_name = f"output_{index}.txt"
        # Əgər fayl artıq mövcuddursa üzərinə yazılacaq
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Fayl yazılarkən xəta baş verdi {file_name}: {e}")
