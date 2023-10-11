
def dark_mode_context(request):
    # Отримати стан темного режиму з сесії
    dark_mode = request.session.get('dark_mode', 'off')
    
    # Повернути словник, який буде додано до контексту
    return {'dark_mode': dark_mode}
