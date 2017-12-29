class SubTitleItem:

    '''a class to restore subtitle item'''

    def __init__(self, order, start_time, end_time, contents):
        self.order = order
        self.start_time = start_time
        self.end_time = end_time
        self.contents = contents


    def set_order(self, order):
        self.order = order

    def generate_writable_contents(self):
        items = []
        items.append(repr(self.order) + '\n')
        items.append(self.start_time + ' --> ' + self.end_time + '\n')
        for c in self.contents:
            items.append(c + '\n')
        items.append('\n')
        return items


class SubTitle:

    def __init__(self, path):
        self.subtitle_items = []
        self.ordered_subtitle_items = []
        with open(path, 'r', encoding='utf-8') as srt_file:
            order = start_time = end_time = None
            contents = []
            for line in srt_file:
                line = line.strip()
                if not line:
                    if not contents and not start_time and not order:
                        continue
                    else:
                        item = SubTitleItem(order, start_time, end_time, contents)
                        self.subtitle_items.append(item)
                        order = start_time = end_time = None
                        contents = []
                elif not order:
                    order = eval(line)
                elif not start_time and not end_time:
                    times = line.split(' ')
                    start_time = times[0]
                    end_time = times[2]
                else:
                    contents.append(line)

    def order_by_starttime(self):
        self.ordered_subtitle_items = sorted(self.subtitle_items, key=lambda x: x.start_time)
        order = 1
        for item in self.ordered_subtitle_items:
            item.set_order(order)
            order += 1

    def generate_ordered_subtitle_file(self, path):
        if not self.ordered_subtitle_items:
            return
        with open(path, 'w', encoding='utf-8') as f:
            for item in self.ordered_subtitle_items:
                writes = item.generate_writable_contents()
                f.writelines(writes)

def main():
    st = SubTitle('sample.srt')
    st.order_by_starttime()
    st.generate_ordered_subtitle_file('ordered.srt')


if __name__ == '__main__':
    main()






