Nama : Elvis

NPM : 2506544990

Kelas : PBP b

### Tugas 1

1. saya menggunakan section, tetapi jika dikatakan membantu, sebenarnya tag section tersebut menurut saya hanya membantu dalam hal membedakan bagian dengan lebih cepat, selain dari itu, saya menggunakan div karena secara teknis menurut saya kedua tag tersebut memberikan hasil yang sama. Saya tidak mempunyai alasan tertentu untuk menggunakan div, hal tersebut hanya menjadi kebiasaan saja.
2. tantangan yang saya temukan sebenarnya cukup banyak, seperti konsep grid, yang pada akhirnya konsep tersebut saya terapkan beberapa eksperimen sehingga, jika saya deskripsikan berdasarkan eksperimen saya, grid itu mirip seperti excel, hanya saja bedanya mungkin ialah pada konsep "grid in a grid" yang saya terapkan. 
3. repetisi yang memungkinkan saya untuk mudah keliru dalam building suatu section, seperti experience card di web saya. fungsionalitas dinamis yang ingin saya terapkan sejujurnya ialah data entry yang memungkinkan untuk bermanfaat dalam building dan menghilangkan repetisi, sehingga website tersebut dapat saya build dengan konsep "hanya mengisi template".


### AI Disclosure
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