class Student:
    def __init__(self, name, username, period=None, id=None):
        if name is None or username is None:
            raise ValueError("name and username are required")
        self.name = name
        self.username = username
        self.period = period
        self.id = id

    def __eq__(self, other):
        return isinstance(other, Student) and vars(self) == vars(other)

    def __repr__(self):
        return f"Student({self.name!r}, {self.username!r}, {self.period!r}, {self.id!r})"


class Roster:
    FIELDS = 4

    def __init__(self):
        self.students = {}

    def add(self, student):
        self.students[student.username] = student

    def remove(self, username):
        self.students.pop(username, None)

    def get(self, username):
        return self.students.get(username)

    @staticmethod
    def _encode(value):
        if value is None:
            return "-1#"
        s = str(value)
        return f"{len(s)}#{s}"

    @staticmethod
    def _decode_fields(s):
        fields, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            if j == -1:
                raise ValueError(f"missing '#' at index {i}")
            length = int(s[i:j])
            if length == -1:
                fields.append(None)
                i = j + 1
                continue
            if length < 0 or j + 1 + length > len(s):
                raise ValueError(f"bad length at index {i}")
            fields.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return fields

    def serialize(self):
        parts = []
        for st in self.students.values():
            for value in (st.name, st.username, st.period, st.id):
                parts.append(self._encode(value))
        return "".join(parts)

    def deserialize(self, s):
        fields = self._decode_fields(s)
        if len(fields) % self.FIELDS:
            raise ValueError("field count is not a multiple of 4")
        students = {}
        for k in range(0, len(fields), self.FIELDS):
            name, username, period, id = fields[k : k + self.FIELDS]
            st = Student(
                name,
                username,
                int(period) if period is not None else None,
                int(id) if id is not None else None,
            )
            students[st.username] = st
        self.students = students


r = Roster()
r.add(Student("Alice", "alice1", 3, 1001))
r.add(Student("O;Brien", "ob#2"))
r.add(Student("", "empty_name", None, 0))
r.add(Student("12#34", "digits", 7))
s = r.serialize()
print(s)

r2 = Roster()
r2.add(Student("Stale", "stale"))
r2.deserialize(s)
print(list(r2.students.values()))
print(list(r2.students.values()) == list(r.students.values()))
print(r2.get("stale"))

empty = Roster()
print(repr(empty.serialize()))
empty.deserialize("")
print(empty.students)

for bad in ["5#Alice", "3#abc2#xy-1#-1#9#short", "-1#5#alice-1#-1#", "abc"]:
    try:
        Roster().deserialize(bad)
    except ValueError as e:
        print("error:", e)

r3 = Roster()
r3.add(Student("Keep", "keep"))
try:
    r3.deserialize("5#Alice")
except ValueError:
    pass
print(list(r3.students.values()))
