# job-project-scraping
 book scraper service with Scrapy and MongoDB

# KURULUM
Kurulum için bilgisayarınızda Docker bulunmalıdır.
- Docker'ı çalıştırın
- app klasörü içerisindeki `.env.example` dosyasının adını `.env` olarak değiştirin
- app klasörü içerisinde bir terminal açın ve `docker-compose up` komutunu çalıştırın
internet hızınıza bağlı olarak 3 dakika içerisinde sistem hazır olacak.
Sistemin hazır olup olmadığını görmek için terminalde `docker ps` yazın, Status kısmı `Up` ya da `Up About a minute` ise sistem hazır demektir.
Tarayıcınızla http://localhost:8000 adresine giderek scraper ui'ı görüntüleyebilirsiniz.
# INSTALLATION
Download, install and run docker on your computer. Then change the `.env.example` file in the app folder to `.env` , then open a terminal in the app folder and run the "docker-compose up" command. after about 3 minutes go to http://localhost:8000 in your browser.
# KULLANIM
- http://localhost:8000 adresine giderek scraper ui'a erişin
- GO TO SCRAPING PAGE'e tıklayarak veri kazıma sayfasına gidin
- Text alanına aramak istediğiniz query'i yazın,
- Checkboxlardan istediğiniz siteleri seçin,
- Scrape butonuna tıkladığınızda scraping status: ok yazısı çıktığında verileriniz kazınmaya başlayacak,
- Kazıma işlemi arkaplanda devam edecek, (şimdilik kazıma işleminin ne durumda olduğu gösterilmiyor)
- Tekrar http://localhost:8000 adresine giderek veri kazıma sayfasında yazdığınız query'nin aynısını yazın ve search'e basın,
- Kazınan veriler console'a yazılacak.
# USAGE
You can query for the data you scraped by going to http://localhost:8000. You can go to the data scraping page by clicking "GO TO SCRAPING PAGE".
The query result is written to the console for now.

# MONGODB'ye erişim
MongoDBCompass ile mongodb://apiuser:apipass@localhost:27017/test adresine bağlanarak mongodb içeriğini görüntüleyebilirsiniz. herhangi bir veri kazımadığınızda db boş olacaktır.

# Kullanılan teknolojiler
- DOCKER
- PYTHON DOCKER IMAGE
- POETRY (PAKET VERSİYON YÖNETİMİ)
- PYHON LIBRARIES AND FRAMEWORKS
  - SCRAPY
  - SCRAPYD
  - SCRAPYD-CLIENT
  - FASTAPI
  - PYDANTIC
  - POETRY

# TECHSTACK
- DOCKER
- PYTHON DOCKER IMAGE
- POETRY (PACKAGE VERSION MANAGEMENT, Similar to package.json, package-lock.json in Node.js)
- PYHON LIBRARIES AND FRAMEWORKS
  - SCRAPY
  - SCRAPYD
  - SCRAPYD-CLIENT
  - FASTAPI
  - PYDANTIC
  - POETRY