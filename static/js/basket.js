$(document).ready(function() {
  $('.remove-from-cart-button').click(function(e) {
    e.preventDefault();
    var product_id = $(this).data('product-id');

    $.ajax({
      type: 'POST',
      url: '/basket/remove' + product_id,
      data: {
        csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      success: function(data) {
        if (data.success) {
          // Обновите содержимое корзины на странице без перезагрузки
          // Например, обновите общее количество товаров в корзине и их общую стоимость

          // Пример обновления общего количества товаров в корзине
          var totalQuantityElement = $('.total-quantity');
          totalQuantityElement.text(data.total_quantity);

          // Пример обновления общей стоимости
          var totalAmountElement = $('.total-amount');
          totalAmountElement.text(data.total_amount);

          // Удалите строку с товаром из таблицы корзины на странице
          $('#cart-table tbody tr[data-product-id="' + product_id + '"]').remove();
        }
      }
    });
  });
});