describe('template spec', () => {
  beforeEach(() =>{
    cy.visit ('https://www.saucedemo.com')
  }
)
  it('вводит данные в поля логина и пароля', () => {
    // Переход на страницу
    cy.visit('https://www.saucedemo.com');

    // Ввод логина
    cy.get('input[name="user-name"]').type('standard_user');

    // Ввод пароля
    cy.get('input[name="password"]').type('secret_sauce');

    // Отправка формы
    cy.get('input[type="submit"]').click();
  });

  it('сортировка', () => {
    cy.get('input[name="user-name"]').type('standard_user');

    // Ввод пароля
    cy.get('input[name="password"]').type('secret_sauce');

    // Отправка формы
    cy.get('input[type="submit"]').click();
    // Убедитесь, что страница загружена
    cy.wait(1000); // Задержка на 1 секунду

    // Сортировка по возрастанию цены
    cy.get('.product_sort_container').select('lohi')
    cy.wait(1000) // Добавлена задержка
    cy.get('.inventory_item_price').then(($prices) => {
      const prices = $prices.map((index, html) => parseFloat(html.innerText.replace('$', ''))).get()
      const sortedPrices = [...prices].sort((a, b) => a - b)
      expect(prices).to.deep.equal(sortedPrices)
    })

    // Сортировка по убыванию цены
    cy.get('.product_sort_container').select('hilo')
    cy.wait(1000) // Добавлена задержка
    cy.get('.inventory_item_price').then(($prices) => {
      const prices = $prices.map((index, html) => parseFloat(html.innerText.replace('$', ''))).get()
      const sortedPrices = [...prices].sort((a, b) => b - a)
      expect(prices).to.deep.equal(sortedPrices)
    })
  });

  it('Нажатие на кнопки добавления в корзину двух товаров и оформление заказа', () => {
    // Убедитесь, что страница загружена
    cy.get('input[name="user-name"]').type('standard_user');

    // Ввод пароля
    cy.get('input[name="password"]').type('secret_sauce');

    // Отправка формы
    cy.get('input[type="submit"]').click();
    cy.wait(1000); // Задержка на 1 секунду

    // Нажатие на кнопки добавления в корзину
    cy.get('.btn.btn_primary.btn_small.btn_inventory').eq(0).click();
    cy.get('.btn.btn_primary.btn_small.btn_inventory').eq(1).click();

    // Переход к корзине
    cy.scrollTo('top');
    cy.get('.shopping_cart_link').click();

    // Оформление заказа
    cy.get('.checkout_button').click();
    cy.get('input[name="firstName"]').type('standard_user');
    cy.get('input[name="lastName"]').type('standard_user');
    cy.get('input[name="postalCode"]').type('1337');
    cy.get('.btn_action').click();

    // Возврат в корзину
    cy.scrollTo('bottom');
    cy.get('.cart_button').click();
  });
});

