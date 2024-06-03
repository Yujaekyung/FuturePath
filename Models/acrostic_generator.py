from typing import Literal

from pydantic import BaseModel, Field

MAX_LENGTH = 20  


class InputModel(BaseModel):
    major: str = Field(
        alias='major',
        description='현재 재학 중인 학과를 입력해주세요!',
        default='컴퓨터공학',
        min_length=1,
        max_length=MAX_LENGTH,
        pattern=rf'^[a-zA-Z가-힣\s]{{1,{MAX_LENGTH}}}$',
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    career_suggestions: str = Field(
        description='학과에 맞는 진로 제시',
    )