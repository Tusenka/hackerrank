from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int
    name: str = "Jane Doe"

    model_config = ConfigDict(str_max_length=10)


user = User(id=1, name="Jane Doe")
for i in user:
    print(i)
