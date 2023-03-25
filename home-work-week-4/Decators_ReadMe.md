* ### **@pytest.fixture:**
> _Test işlemlerinden önce gerekli olan verileri sağlayacak kodun çalışmasını sağlayan yapıdır. ( Veritabanı bağlantısını sağlamak, İşlem yapılacak dataları sağlamak vb.)_

* ### **@pytest.mark.order:**
> _Test işlemleri sırasında belirlediğimiz sıralamaya göre fonksiyonların çalışmasını sağlayan yapıdır. Numara ile sıralandırabildiğimiz gibi diğer testlerin sonucuna göre de sıralama işlemlerini yapmamızı sağlayan yapıdır._

* ### **@pytest.mark.skip:**
> _Test işlemleri sırasında belirtilen fonksiyonun, çalışmadan es geçilmesini sağlayan yapıdır._

* ### **@pytest.mark.parametrize:**
> _Bir test fonksiyonunun farklı parametreler kullanılarak tekrar tekrar çalıştırılmasını sağlayan yapıdır. ( Farklı kullanıcı bilgileri ile giriş yapmayı denemek vb. )_

* ### **@pytest.mark.timeout:**
> _Test işlemleri sırasında belirtilen fonksiyonların çalışma hızını tespit eder ve çok uzun süren sürelerde çalışmayı durdurabilmesini sağlayan yapıdır._

* ### **@pytest.mark.xfail:**
> _Test işlemleri sırasında belirtilen fonksiyonun, hata vermesinin mümkün olduğunu belirtir. Yani fonksiyon hata verdiğinde bize bildirilmeden es geçilmesini sağlayan yapıdır._
