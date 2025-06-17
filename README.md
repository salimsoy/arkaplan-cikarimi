Bu projede, bir görüntüde yer alan kiviler filtrelenerek yalnızca kivilerin beyaz, arka planın ise tamamen siyah olduğu bir çıktı elde edilmiştir. İşlem sonucunda yapraklar görüntüden ayıklanarak sadece kiviler görselde bırakılmıştır.
Proje kapsamında şu adımlar uygulanmıştır:
İlk olarak, giriş görüntüsü gri tonlamaya dönüştürülmüş ve ardından kenarların daha belirgin hale gelmesi için Canny kenar algılama algoritması kullanılmıştır. Bu adım, görüntüdeki nesnelerin dış hatlarını belirlemek açısından kritik bir rol oynamıştır.
Alternatif olarak adaptif thresholding yöntemi de denenmiştir; ancak bu yöntemin kenarları yeterince net ayırt edemediği görülmüş ve bu nedenle Canny yöntemi tercih edilmiştir.
Kenar tespitinden sonra, konturlar arasında oluşabilecek boşlukları gidermek amacıyla morfolojik kapatma (closing) işlemi uygulanmıştır. Bu adım sayesinde yakındaki kenarlar birleştirilerek daha sağlam ve bütünsel konturlar elde edilmiştir.
Daha sonra, cv2.findContours() fonksiyonu kullanılarak konturlar tespit edilmiştir. 
Bu konturlar, görüntüdeki tüm nesnelerin dış hatlarını temsil eder. Ancak, projede yalnızca kiviler hedef alındığı için, konturlar üzerinde bir filtreleme işlemi yapılmıştır. for döngüsü ile konturlar tek tek kontrol edilerek yaprak gibi istenmeyen bölgeler elenmiştir.
Filtrelenmiş konturlar elde edildikten sonra, sıfırlardan oluşan boş bir maske üzerinde bu konturlar çizilmiştir. 
Sonuç olarak, yalnızca kivileri içeren ve arka planı tamamen siyah olan ikili (binary) bir maske görüntüsü oluşturulmuştur. Bu maske, projenin nihai hedefi olan sadeleştirilmiş görüntüyü temsil etmektedir.
