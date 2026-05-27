from graphviz import Digraph

dot = Digraph(comment='BPMN IT Equipment Issuance Process')
dot.attr(rankdir='TB')
dot.attr('node', shape='box', style='rounded', fontsize='10')


dot.node('start', 'Начало\n(Пользователю нужно оборудование)',
         shape='ellipse', style='filled', fillcolor='white')


dot.node('user_request', 'Пользователь делает заявку\n(почта/телефон) в 1-ю линию техподдержки')
dot.edge('start', 'user_request')


dot.node('get_ticket', 'Пользователь получает номер обращения')
dot.edge('user_request', 'get_ticket')

dot.node('support_create_req', '1-я линия создаёт заявку\nна оборудование в системе №2\n(отдел снабжения)')
dot.edge('get_ticket', 'support_create_req')


dot.node('supply_accept', 'Отдел снабжения принимает заявку\nв системе №2\n(уведомление в почте + экран ЛК)')
dot.edge('support_create_req', 'supply_accept')

dot.node('check_stock', 'Проверка наличия оборудования\nв системе №3')
dot.edge('supply_accept', 'check_stock')

dot.node('gateway_stock', 'Оборудование есть?',
         shape='diamond', style='filled', fillcolor='lightgray')
dot.edge('check_stock', 'gateway_stock')


dot.node('yes_stock', 'Да', shape='plaintext')
dot.edge('gateway_stock', 'yes_stock', label='Да')

dot.node('logistics_call_yes', 'Снабжение вызывает логистику')
dot.edge('yes_stock', 'logistics_call_yes')

dot.node('send_to_support_yes', 'Отправляет оборудование\n1-й линии техподдержки')
dot.edge('logistics_call_yes', 'send_to_support_yes')

dot.node('no_stock', 'Нет', shape='plaintext')
dot.edge('gateway_stock', 'no_stock', label='Нет')

dot.node('purchase_req', 'Снабжение делает заявку\nна закупку поставщику (почта)')
dot.edge('no_stock', 'purchase_req')

dot.node('wait_equipment', 'Ждёт оборудование')
dot.edge('purchase_req', 'wait_equipment')

dot.node('supplier_deliver', 'Поставщик привозит оборудование')
dot.edge('wait_equipment', 'supplier_deliver')

dot.node('receive_stock', 'Снабжение проводит приём\nоборудования в системе №3')
dot.edge('supplier_deliver', 'receive_stock')

dot.node('logistics_call_no', 'Снабжение вызывает логистику')
dot.edge('receive_stock', 'logistics_call_no')

dot.node('send_to_support_no', 'Передаёт оборудование\nтехподдержке')
dot.edge('logistics_call_no', 'send_to_support_no')

dot.node('merge_paths', '', shape='point')
dot.edge('send_to_support_yes', 'merge_paths')
dot.edge('send_to_support_no', 'merge_paths')


dot.node('support_issue', 'Техподдержка выдаёт оборудование\nпользователю')
dot.edge('merge_paths', 'support_issue')

dot.node('close_requests', 'Техподдержка закрывает заявку:\n- в системе №1\n- в системе №2')
dot.edge('support_issue', 'close_requests')

dot.node('user_gets', 'Пользователь получает оборудование')
dot.edge('close_requests', 'user_gets')


dot.node('rating', 'Пользователь может выставить оценку\nсервиса технической поддержке')
dot.edge('user_gets', 'rating')


dot.node('end', 'Конец', shape='ellipse', style='filled', fillcolor='white')
dot.edge('rating', 'end')

dot.render('output/bpmn_it_equipment_process', format='png', cleanup=True)
print("BPMN диаграмма сохранена в output/bpmn_it_equipment_process.png")