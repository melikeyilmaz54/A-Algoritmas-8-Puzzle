# A-Algoritmas-8-Puzzle
8-Puzzle problemini A* algoritması ile çözen kod ve akış
A* algoritması, durumları keşfederken her bir durum için maliyeti ve hedefe olan tahmini uzaklığı (heuristic) birleştirerek en iyi çözüm yolunu bulur.
g(n): Başlangıçtan bu duruma kadar gelen gerçek yol maliyeti (adım sayısı).
h(n): Heuristic fonksiyon; yanlış yerde olan blokların sayısı (misplaced tiles) heuristi kullanıyor.
f(n) = g(n) + h(n): Toplam tahmini maliyet.
