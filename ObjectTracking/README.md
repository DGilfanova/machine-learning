# Object detector

```
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
```

Отделяет фон от потенциальных объектов по Gaussian mixture model background subtraction

Это задача извлечения статического фона из последовательности видеокадров.  

После того как фон был смоделирован, обычно используется метод, называемый вычитанием фона, который позволяет извлекать передний план изображения для дальнейшей обработки (распознавание объектов).  

Входное видео (roadway.mp4) : транспортные средства занимают здесь передний план, и их динамический характер объясняет изменение уровней интенсивности точек на дороге.  

Мы собираемся смоделировать каждую точку в пространстве для всех трех каналов изображения, а именно R, G и B, как бимодальное распределение гауссов, где один гауссиан в смеси приходится на фон, а другой на передний план.


> ### Алгоритм:
> 
> 1. Извлеките кадры из видео.
> 2. Сложите кадры в массив, где будут определены конечные размеры массива (num_frames, image_width, image_height num_channels)
> 3. Инициализируйте фиктивное фоновое изображение того же размера, что и отдельные кадры.
> 4. Для каждой точки, характеризующейся координатой x, координатой y и каналом, моделируйте значение интенсивности во всех кадрах как смесь двух гауссов.
> 5. После моделирования инициализируйте значение интенсивности в соответствующем месте на фиктивном фоновом изображении со средним значением наиболее взвешенного кластера. Наиболее взвешенным кластером будет тот, который исходит из фона, тогда как из-за динамически изменяющегося и разреженного характера переднего плана другой кластер будет иметь меньший вес.
> 6. Наконец, фоновое изображение будет содержать значения интенсивности, соответствующие статическому фону.


## Video: 
[youtube](https://youtu.be/hreWtTESLFs)
