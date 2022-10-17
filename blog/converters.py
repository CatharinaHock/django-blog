class IntListConverter:
    regex = '"["[0-9,]+ "]" '

    def to_python(self, value):
        value_list=[]
        current_element=""
        for char in value:
            if char in ["[", "]"]:
                continue
            if char == ",":
                value_list.append(int(current_element))
                current_element = ""
            else:
                current_element += char
        return value_list

    def to_url(self, value):
        return str(value)