import tcod as libtcod
from input_handlers import handle_keys

def main():
    # print('Hello World!')
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width/2)
    player_y = int(screen_height/2)

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'B.U.D.D.', False)

    con = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key()  # cualquier tecla
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        # donde esta con solía ser 0 (la consola por predeterminado)
        libtcod.console_set_default_foreground(con, libtcod.yellow)  # color del simbolo
        libtcod.console_put_char(con, player_x, player_y, 'D', libtcod.BKGND_NONE)  # posicion del simbolo
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libtcod.console_flush()  # muestra lo que hay en la pantalla

        libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)  # vuelve vacio donde estabamos
        # se hace antes de cambiar de posicion, porque o si no, va a volver vacío donde vamos a estar
        # key = libtcod.console_check_for_keypress()

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move  # los valores del vector
            player_x += dx
            player_y += dy

        # if key.vk == libtcod.KEY_ESCAPE:  # si se presiona escape, salir
        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())



if __name__ == '__main__':
    main()