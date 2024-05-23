import EscapeRout as er

if __name__ == '__main__':
    # 出口
    dest = (77, 672)
    # 起点
    source_coordinates = [(238, 324), (245, 350)]
    er.get_escape_route(dest, source_coordinates)
