import EscapeRout as er

if __name__ == '__main__':
    # 出口
    dest = (150, 400)
    # 起点
    source_coordinates = [(290, 324), (290, 350)]
    er.get_escape_route(dest, source_coordinates)
