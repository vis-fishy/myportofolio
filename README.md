Nama : Elvis

NPM : 2506544990

Kelas : PBP b

### Tugas 1

1. saya menggunakan section, tetapi jika dikatakan membantu, sebenarnya tag section tersebut menurut saya hanya membantu dalam hal membedakan bagian dengan lebih cepat, selain dari itu, saya menggunakan div karena secara teknis menurut saya kedua tag tersebut memberikan hasil yang sama. Saya tidak mempunyai alasan tertentu untuk menggunakan div, hal tersebut hanya menjadi kebiasaan saja.
2. tantangan yang saya temukan sebenarnya cukup banyak, seperti konsep grid, yang pada akhirnya konsep tersebut saya terapkan beberapa eksperimen sehingga, jika saya deskripsikan berdasarkan eksperimen saya, grid itu mirip seperti excel, hanya saja bedanya mungkin ialah pada konsep "grid in a grid" yang saya terapkan. 
3. repetisi yang memungkinkan saya untuk mudah keliru dalam building suatu section, seperti experience card di web saya. fungsionalitas dinamis yang ingin saya terapkan sejujurnya ialah data entry yang memungkinkan untuk bermanfaat dalam building dan menghilangkan repetisi, sehingga website tersebut dapat saya build dengan konsep "hanya mengisi template".


### AI Disclosure Tugas 1
saya menggunakan chat gpt versi web untuk membantu dan memperbaiki beberapa bagian (mostly css) serta memberikan inspirasi terhadap design.

1.  https://chatgpt.com/share/6a9ed200-7c40-83ec-8f55-56dbba21127f (dropdown/switchlike behavior card)

Pada bagian experience card, untuk style pembuatan, saya meminta untuk chat gpt menyediakan cara yang bisa saya tempuh untuk menerapkan dropdown dan switchlike behavior pada experience card. beberapa komponen yang dibuatnya antara lain: 

code yang terdapat dalam /static/js/script.js (pernah diusahakan untuk modifikasi, tetapi after some consideration menurut saya kodingan seperti itu sudah cukup bagus)

css dengan class "experience-*" dengan konteks card (sudah dimodifikasi berdasarkan keinginan sendiri)


2. https://chatgpt.com/share/6a9d50db-ef68-83ec-8fa8-99f80a34e591 (sticky navbar)

pada bagian ini, saya mencari cara agar ketika user scroll ke bawah, tidak perlu dilakukan scroll kembali keatas atau refresh untuk kembali ke awal page. disini chatgpt menyarankan untuk memodifikasi attb position, top, dan z-index.

3. https://chatgpt.com/share/6a9d5738-7fdc-83ec-8194-686b6d457f6a (preventing grid overlap)

sebelumnya saya menemukan suatu masalah, dimana terdapat komponen yang saling overlap, dan pada chat ini saya meminta chatgpt untuk membantu menyelesaikan masalah ini. dari chat inilah saya memperoleh konsep baru yang menurut saya cukup berguna, dimana jika saya deskripsikan dalam beberapa kata, bisa saya katakan seperti "grid in a grid"

4. https://chatgpt.com/share/6a9d6f91-35c8-83ec-9502-a48b9f639270 (element hover transition)

sebenarnya pada chat ini, saya awalnya sudah memiliki pemikiran sendiri, yaitu memanfaatkan border. tetapi pada akhir cara tersebut saya tinggalkan karena memiliki efek samping memakan layout page. pada akhirnya saya meminta chat untuk mencarikan alternatif, dan diperolehlah metode outline.

5. https://chatgpt.com/share/6a9d6fb1-485c-83ec-982e-6d62abb8f63b (removing scrollbar from view)

pada chat ini, saya awalnya merasa bahwa pada platform web desktop, terlihat scrollbar memakan layout page yang saya notice melalui sedikit offset kekiri pada web saya berdasarkan penglihatan saya. dari sini saya meminta chatgpt untuk mencarikan metode untuk menghilangkan scrollbar tersebut. hasilnya dapat dilihat pada css yang memiliki tag html pada file /static/css/style.css

6. https://chatgpt.com/share/6a9d6fdc-f2d8-83ec-a2b2-39e5d59c6b46 (first prototype by ai)

pada chat ini sebenarnya saya hanya ingin mencari inspirasi dan melihat sebuah prototype, yang mana pada awalnya merupakan struktur 2 col. tetapi pada akhirnya saya tinggalkan struktur tersebut karena terinspirasi oleh web portofolio mentor dulunya. yang saya adopsi pada chat ini ialah beberapa metode, salah satunya konsep reuse yang diterapkan pada sebagian komponen. chat ini kemungkinan besar tanpa saya sadari menginfluence saya dalam hal design preference pada web saya.

### Tugas 2

1. Pertama user akan membuka link menuju server, dan dari link tersebut, user melakukan http request ke server django. Request tersebut kemudian diterima oleh file urls.py di root proyek. Ibarat pintu masuk utama yang membuka jalan ke pintu lainnya, urls.py akan menyeleksi request berdasarkan pattern yang ada. Pada proyek portofolio ini, isi dari root file urls.py ialah pattern untuk memperoleh response admin dan sebuah pintu masuk baru (urls.py pada app main). Ekspektasi kita ialah link user tidak menuju ke admin site, sehingga request akan diteruskan ke urls.py milik app main. Pada file tersebut, akan dicari lagi pattern yang sesuai, dan jika didapat pattern yang diinginkan, akan terdapat fungsi yang dijalankan, dimana fungsi tersebut juga akan menerima request yang telah diteruskan kepada urls.py. biasanya fungsi tersebut disimpan didalam file views.py, sehingga yang di letakkan sebagai aksi untuk pattern dalam urls.py ialah sebuah reference menuju fungsi tersebut. Kembali lagi ke views.py, fungsi yang telah dipanggil tersebut akan merancang sebuah response (rendering) berdasarkan beberapa hal seperti data perancang web yang berdasarkan suatu model yang disimpan dalam file models.py milik app. biasanya response tersebut tidak dirancang dari 0, melainkan terdapat sebuah template yang dirancang di root directory untuk dapat digunakan sebagai template pembuatan web yang kemudian diisikan data-data yang telah tersimpan dalam database.
2. jika di tuliskan langsung dalam template, maka setiap penambahan data baru pada web akan memerlukan waktu dan langkah yang lebih banyak, tetapi jika dituliskan dalam bentuk suatu model, maka kita sebagai developer memperoleh kemudahan dimana jika terdapat data baru, kita hanya perlu menulisnya berdasarkan model tersebut ke dalam database. hal ini sangat mengurangi waktu development karena dengan scenario tersebut, kita bisa menempuhnya dengan cara tidak mengulangi suatu blok kode dan hanya melakukan automasi. 
3. perbedaan makemigrations dan migrate bisa kita ibaratkan seperti pembuatan blueprint dan penyimpanan blueprint, dimana makemigrations awalnya akan melakukan pembuatan atau peng-update-an blueprint berdasarkan perubahan yang ada pada model, jika diperlukan. sedangkan migrate itu sendiri melakukan aksi penyimpanan kedalam database sehingga setiap object yang sudah ada dalam database, perlu mengikuti blueprint yang sudah berubah itu. contoh perubahan model yang mengharuskan kita untuk menjalankan kedua fungsi tersebut ialah ketika kita menambahkan sebuah field baru dalam model.

### AI Disclosure Tugas 2
saya menggunakan chat gpt versi web untuk membantu memberikan inspirasi terhadap design serta cara mengimplementasikan suatu design.

https://chatgpt.com/share/6aa812cc-3584-83ec-af5b-4b223df9ebac (masonry layout)

### Tugas 3

1. ModelForm digunakan karena dapat membuat form Django yang terhubung langsung dengan model yang sudah dibuat dalam models.py sehingga kita tidak perlu mendefinisikan setiap field secara manual di HTML dan melakukan validasi sendiri. Hal ini membuat kode lebih singkat, konsisten, dan mengurangi kemungkinan kesalahan dibandingkan membuat form HTML secara manual. Sementara itu, csrf token digunakan untuk menghindari terjadinya cross site request forgery. Django memberikan token unik pada form sehingga ketika request POST dikirim, Django dapat memeriksa apakah request tersebut benar-benar berasal dari form yang dibuat oleh aplikasi tersebut.
2. karena format yang digunakan dalam penulisan JSON itu lebih sederhana dan lebih mirip dengan format syntax yang digunakan pada sebagian besar bahasa pemrograman. jika dibandingkan dengan XML, XML memerlukan banyak tag berbeda seperti menuliskan HTML, dan hal tersebut menyebabkan potensi terjadi typo semakin tinggi.
3. Client atau aplikasi mengirim request ke URL yang terhubung dengan view dan mengarah ke fungsi yang seharusnya mengembalikan data dalam format json. Dalam fungsi tersebut, biasanya django akan mengumpulkan data yang diinginkan oleh request, dan karena data tersebut biasanya masih dalam bentuk object Models milik django, perlu dilakukan serialize terlebih dahulu. Proses serialize akan mengubah setiap field dan valuenya menjadi format json dalam bentuk key value pair. Setelah proses serialize selesai, data tersebut barulah di kembalikan dalam bentuk HttpResponse ke pengguna, dan kemudian dapat digunakan untuk ditampilkan dalam frontend atau aplikasi lain. Proses serialization diperlukan karena object Models pada django memiliki struktur dan perilaku yang berbeda dengan format json pada umumnya, sehingga diperlukan serialization menjadi format yang sesuai.

### AI Disclosure Tugas 3
saya menggunakan chat gpt versi web untuk membantu dalam memikirkan metode yang tepat dalam mengimplementasikan edit delete dan button layout serta password implementation.

https://chatgpt.com/share/6ab15516-412c-83ec-8dfb-86b2b6ed42c6 (password field and a bit of delete button layout)

https://chatgpt.com/share/6ab1557f-3bdc-83ec-bd5f-cb0bfb1c9c97 (delete cert request handling)

https://chatgpt.com/share/6ab155a8-df70-83ec-a546-3dbebd2546bb (edit cert request handling)