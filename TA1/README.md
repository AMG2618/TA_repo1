# 🧪 TA1 - Testare Automată cu Behave și Selenium

Acest proiect conține teste automate pentru aplicația web `https://probaamg.rdsweb.ro`, folosind framework-ul **Behave** (BDD) și **Selenium WebDriver** pentru interacțiunea cu browserul.

---

## 📁 Structura Proiectului
```plaintext
TA1/
    features/
        1_sign_up.feature
        2_sign_up-user_error.feature
        3_login.feature
        4_incarca_document.feature
        5_verifica_documente_incarcate.feature
        6_descarca_document.feature
        7_cerere_viza_48.feature
        8_cerere_emc_eroare.feature
        9_admin_verificare_cereri_emc.feature
        10_admin_editare_user.feature
        11_admin_stergere_user.feature
    pages/
        1_sign_up.py
        2_sign_up-user_error.py
        3_login.py
        4_incarca_document.py
        5_verifica_documente_incarcate.py
        6_descarca_document.py
        7_cerere_viza_48.py
        8_cerere_emc_eroare.py
        9_admin_verificare_cereri_emc.py
        10_admin_editare_user.py
        11_admin_stergere_user.py
    steps/
         1_sign_up.py
        2_sign_up-user_error.py
        3_login.py
        4_incarca_document.py
        5_verifica_documente_incarcate.py
        6_descarca_document.py
        7_cerere_viza_48.py
        8_cerere_emc_eroare.py
        9_admin_verificare_cereri_emc.py
        10_admin_editare_user.py
        11_admin_stergere_user.py
---

## 🚀 Cum rulezi testele

### 1. Instalează dependințele

Asigură-te că ai Python 3 instalat, apoi rulează:

```bash
pip install -r requirements.txt


----
Descrierea folderelor
steps/: conține pașii definiți în Python pentru fiecare scenariu .feature.

features/*.feature: scenarii scrise în format Gherkin (Given, When, Then).

pages/: acțiuni și funcții reutilizabile pentru interacțiunea cu paginile web.

environment.py: setup și teardown pentru testele Behave (ex. deschiderea browserului).

----
Funcționalități testate
    1. Înregistrare utilizator
    2. Înregistrare utilizator cu eroare
    3. Autentificare utilizator
    4. Încărcare document
    5. Verificare documente încărcate
    6. Descărcare document
    7. Cerere viză EMC cu minim 48 puncte
    8. Cerere viză EMC cu eroare (sub 48 puncte)
    9. Administrator verificare cereri EMC
    10. Administrator editare utilizator
    11. Administrator ștergere utilizator
----