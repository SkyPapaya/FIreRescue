import EscapeRout as er

if __name__ == '__main__':
    # 出口
    dest = (700, 220)
    # 起点
    source_coordinates = [(400, 220)]
    er.get_escape_route(dest, source_coordinates)
