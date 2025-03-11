'''
Converting a dictionary list to html code. From this:
[{"A":"a_1", "B":"b_1", "C":"c_1"},
{"A":"a_2", "B":"b_2", "C":"c_2"}]
Convert to this:
<tr>
    <td>
        <select>
            <option value="A">
            A
            </option>
            <option value="a_1">
            a_1
            </option>
            <option value="a_2">
            a_2
            </option>
        </select>
    </td>
    <td>
        <select>
            <option value="B">
            B
            </option>
            <option value="b_1">
            b_1
            </option>
            <option value="b_2">
            b_2
            </option>
        </select>
    </td>
    <td>
        <select>
            <option value="C">
            C
            </option>
            <option value="c_1">
            c_1
            </option>
            <option value="c_2">
            c_2
            </option>
        </select>
    </td>
</tr>
<tr>
    <td>
        a_1
    </td>
    <td>
        b_1
    </td>
    <td>
        c_1
    </td>
</tr>
<tr>
    <td>
        a_2
    </td>
    <td>
        b_2
    </td>
    <td>
        c_2
    </td>
</tr>'''
# Разработка Data Conversion.
'''
listOfDictionaries = [
        {"A":"a_1", "B":"b_1", "C":"c_1"}, 
        {"A":"a_2", "B":"b_2", "C":"c_2"}
    ]
'''
listOfDictionaries=[]
listOfDictionaries.append({"A":"a_1", "B":"b_1", "C":"c_1"})
listOfDictionaries.append({"A":"a_2", "B":"b_2", "C":"c_2"})
'''
numb=int(input("Enter number: "))
for dictionary in range(1,numb):
    listOfDictionaries.append({"A":"a_$dictionary", "B":"b_$dictionary", "C":"c_$dictionary"})
    print(dictionary)
'''
'''
for dictionary in listOfDictionaries:
    #print(dictionary)
    #print(listOfDictionaries[0]['A'])
    for k in dictionary:
        print(k)
    for v in dictionary:
        print(dictionary[v])
'''
html="""{0}"""
tr="<tr>{0}</tr>"
td="<td>{0}</td>"
dictionary=[tr.format(''.join([td.format(a) for a in item])) for item in listOfDictionaries[:1]]
dictionary.extend([tr.format(''.join([td.format(item[a]) for a in item])) for item in listOfDictionaries])
print (html.format("".join(dictionary)))