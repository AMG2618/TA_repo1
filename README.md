 === LIBRARII de INSALAT ===
 - Selenium
 - Behave
 - Behave-hTML-Formatter
---
 === PLUGIN DE INSTALAT ===
 - gherkin 
 - ini

=== STRUCTURA FOLDERE SI FISIERE ===
- features
  - pages
- resources
- steps
- behave.ini
- browser.py
- environment.py
- README.md
- requirements.txt

 === COMENZI EXECUTIE TESTE ===
- behave (executa toate testele)
- behave --tags=login (executa toate testele cu tag-ul 'login')
- behave --tags=signUP (executa toate testele cu tag-ul 'signUP')
- behave --tags=login, smoke (executa toate testele cu tag-urile 'login' sau 'smoke')
- behave -f behave_html_formatter:HTMLFormatter -o report01.html --tags=login (genereaza raport HTML)
Acest proiect conține teste automate pentru aplicația web `https://probaamg.rdsweb.ro`, folosind framework-ul **Behave** (BDD) și **Selenium WebDriver** pentru interacțiunea cu browserul.

---

## 📁 Structura Proiectului
```plaintext
TA_exam2
    features/
        login.feature
        upload.feature
        pages/
            base_page.py
            login_page.py
            sign_up_page.py
    steps/
        login_steps.py
        sign_up_steps.py
        upload_doc_steps.py
    resources/
        image.jpg
        UploadTestDoc.pdf
    behave.ini
    browser.py
    environment.py
    README.md
    requirements.txt
```

## 🚀 Cum rulezi testele

### 1. Instalează dependințele

Asigură-te că ai Python 3 instalat, apoi rulează:

```bash
pip install -r requirements.txt
```
----
Descrierea folderelor
steps/: conține pașii definiți în Python pentru fiecare scenariu .feature.

features/*.feature: scenarii scrise în format Gherkin (Given, When, Then).

pages/: acțiuni și funcții reutilizabile pentru interacțiunea cu paginile web.

environment.py: setup și teardown pentru testele Behave (ex. deschiderea browserului).
