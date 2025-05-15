## [Critical] XSS-уязвимость в форме логина DemoQA

**Шаги воспроизведения**:
1. Открыть https://demoqa.com/login
2. Ввести в поле пароля: `<script>alert(1)</script>`
3. Нажать "Login"

**Ожидаемый результат**: Санитизация ввода  
**Фактический результат**: Выполнение JavaScript-кода

**Скриншот**:  
![XSS Bug](./screenshots/xss-demoqa.png)
