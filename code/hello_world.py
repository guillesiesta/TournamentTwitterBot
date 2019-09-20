from yattag import Doc
import imgkit

f = open("tests/web.html", "w")

doc, tag, text, line = Doc(
    defaults = {'ingredient': ['chocolate', 'coffee']}
).ttl()

with tag('h1'):
    text('Hello world!')
    text('Hello world!')

with tag('h2'):
    text('Caca pedo y culo')


with tag('form', action = ""):
    line('label', 'Select one or more ingredients')
    with doc.select(name = 'ingredient', multiple = "multiple"):
        for value, description in (
            ("chocolate", "Dark Chocolate"),
            ("almonds", "Roasted almonds"),
            ("honey", "Acacia honey"),
            ("coffee", "Ethiopian coffee")
        ):
            with doc.option(value = value):
                text(description)
    doc.stag('input', type = "submit", value = "Validate")

f.write(doc.getvalue())

f.close()

imgkit.from_file('tests/web.html','tests/out.jpg')
