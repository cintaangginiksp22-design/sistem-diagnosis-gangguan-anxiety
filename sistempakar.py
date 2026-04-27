def tanya(pertanyaan):
    while True:
        jawab = input(pertanyaan + " (y/n): ").lower()
        if jawab in ['y', 'n']:
            return jawab == 'y'
        print("Input hanya boleh y atau n")


def diagnosa_anxiety():
    print("======================================================")
    print("   SISTEM PAKAR DIAGNOSA JENIS GANGGUAN ANXIETY")
    print("======================================================")
    print("Petunjuk: Jawab dengan 'y' (Ya) atau 'n' (Tidak)\n")

    diagnosa = []

    # Rule 1: GAD
    print("\n[Deteksi Generalized Anxiety Disorder]")
    if tanya("G1. Apakah Anda khawatir berlebihan tentang masalah sehari-hari?"):
        if tanya("G2. Apakah Anda sulit mengontrol rasa khawatir?"):
            if tanya("G3. Apakah Anda sering sulit berkonsentrasi?"):
                if tanya("G4. Apakah Anda tidak bisa santai dan rileks?"):
                    if tanya("G5. Apakah Anda mudah marah dan kesal?"):
                        diagnosa.append("J1: Generalized Anxiety Disorders (GAD)")

    # Rule 2: Fobia
    print("\n[Deteksi Fobia]")
    if tanya("G6. Apakah detak jantung Anda meningkat saat takut?"):
        if tanya("G7. Apakah Anda gemetar dan berkeringat?"):
            if tanya("G8. Apakah telinga Anda berdengung?"):
                if tanya("G9. Apakah Anda ingin berlari atau sembunyi dari hal yang ditakuti?"):
                    diagnosa.append("J2: Fobia")

    # Rule 3: Social Anxiety
    print("\n[Deteksi Social Anxiety]")
    if tanya("G10. Apakah Anda takut bertemu orang asing?"):
        if tanya("G11. Apakah Anda menghindari percakapan?"):
            if tanya("G12. Apakah Anda khawatir terlihat tidak kompeten?"):
                if tanya("G13. Apakah Anda merasa selalu diawasi orang lain?"):
                    if tanya("G14. Apakah Anda takut mendapat kritikan?"):
                        diagnosa.append("J3: Social Anxiety")

    # Rule 4: PTSD
    print("\n[Deteksi PTSD]")
    if tanya("G16. Apakah Anda merasa putus asa tentang masa depan?"):
        if tanya("G17. Apakah Anda kesulitan mengingat?"):
            if tanya("G18. Apakah Anda merasa jauh dari keluarga dan teman?"):
                if tanya("G19. Apakah Anda mudah kaget?"):
                    if tanya("G20. Apakah Anda selalu waspada terhadap bahaya?"):
                        if tanya("G21. Apakah Anda sulit tidur?"):
                            diagnosa.append("J4: Post-Traumatic Stress Disorder (PTSD)")

    # Rule 5: Panic Attack
    print("\n[Deteksi Panic Attack]")
    if tanya("G15. Apakah Anda mengalami serangan panik?"):
        if tanya("G22. Apakah Anda gelisah atau berpikir tidak masuk akal?"):
            if tanya("G23. Apakah Anda merasa takut berlebihan?"):
                if tanya("G24. Apakah otot tubuh Anda sering tegang?"):
                    if tanya("G25. Apakah Anda gemetar atau menggigil?"):
                        if tanya("G26. Apakah jantung Anda berdebar-debar?"):
                            if tanya("G27. Apakah Anda pusing atau hampir pingsan?"):
                                diagnosa.append("J5: Panic Attack")

    # Rule 6: OCD
    print("\n[Deteksi OCD]")
    if tanya("G28. Apakah Anda takut tertular penyakit atau menyentuh benda asing?"):
        if tanya("G29. Apakah Anda stres melihat benda tidak simetris?"):
            if tanya("G30. Apakah Anda sering mandi atau cuci tangan berulang?"):
                if tanya("G31. Apakah Anda sering mengulang kata dalam hati?"):
                    if tanya("G32. Apakah Anda menghitung kegiatan dengan pola tertentu?"):
                        diagnosa.append("J6: Obsessive Compulsive Disorder (OCD)")

    # Output
    print("\n" + "="*50)
    print("HASIL ANALISA SISTEM PAKAR")
    print("="*50)

    if diagnosa:
        print("Berdasarkan gejala yang dialami, Anda terindikasi:")
        for hasil in diagnosa:
            print("->", hasil)

        print("\nSARAN:")
        print("Sistem ini hanya memberikan diagnosa awal.")
        print("Silakan konsultasi dengan psikolog atau psikiater.")
    else:
        print("Diagnosa tidak ditemukan.")

    print("="*50)


if __name__ == "__main__":
    diagnosa_anxiety()