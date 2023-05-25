body {
    font-family: Arial,  sans-serif; /* Семейство шрифтов */
    font-size: 18px; /* Размер основного шрифта в <p></p>  */
    color:#4d341f ; /* Цвет основного текста */
    background-color:#918fe3; /* Цвет фона веб-страницы */
}
@keyframes color-change {
    0% {
      color: #b56251;
    }

    50% {
      color: #8d5794;
    }

    100% {
      color: #5f90a1;
    }
}

h1:hover{
    animation: color-change 5s infinite;
}
h1 {
    color:#4d341f; /* Цвет заголовка */
    font-size: 35px; /* Размер шрифта в пунктах */
    font-family: Inter, serif; /* Семейство шрифтов */
   }
h2 {
    color:#363559; /* Цвет заголовка */
    font-size: 27px; /* Размер шрифта в пунктах */
    font-family: Inter, serif; /* Семейство шрифтов */
   }
