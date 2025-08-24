 === LIBRARII de INSALAT ===
 - Selenium
 - Behave
 - Behave-hTML-Formatter
---
 === PUGIN DE INSTALAT ===
 - gherkin 
 - ini

=== STRUCTURA FOLDERE SI FISIERE ===
- features
- pages
- steps
- browser.py
- environment.py
- behave.ini

 === COMENZI EXECUTIE TESTE ===
- behave (executa toate testele)
- behave -- tags=login (executa toate testele cu tag-ul 'login')
- behave --tags=login, smoke (executa toate testele cu tag-urile 'login' sau 'smoke')
- behave -f html -o report.html --tags=login (genereaza raport HTML)
Acest proiect conține teste automate pentru aplicația web `https://probaamg.rdsweb.ro`, folosind framework-ul **Behave** (BDD) și **Selenium WebDriver** pentru interacțiunea cu browserul.

---

## 📁 Structura Proiectului
```plaintext
TA1/
    features/
        sign_up.feature
        sign_up_user_error.feature
        login.feature
        upload_document.feature
        verify_docs_uploaded.feature
        download_document.feature
        request_visa_48.feature
        request_visa_error.feature
        admin_verificare_cereri_emc.feature
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
