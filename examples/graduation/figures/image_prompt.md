# 콘셉트 이미지 프롬프트 — 단과대학별 네임콜 수여식 장면

## 넣을 위치 제안
- 표지 바로 아래 또는 "3. 새 프로그램 개요" 첫 문단 위 (심사위원이 글보다 먼저 장면을 보도록)
- 캡션 예: "단과대학 강당에서 졸업생의 이름이 불리고, 단상 아래에서 가족이 그 순간을 찍는다 (AI 생성 예시 이미지)"

## 한국어 설명
- 장소: 단과대학 강당(실내, 계단식 좌석 200~300석 규모). 경암체육관이 아니다.
- 시간대: 2월 오후 2시 무렵. 창으로 들어오는 부드러운 겨울 햇빛 + 무대 조명.
- 카메라: 가족석 앞줄 높이, 무대를 비스듬히(약 30°) 바라보는 35mm 시점. 얕은 심도로 단상 위 두 사람에 초점.
- 장면: 학위복(검정 가운, 보라색 후드) 차림 졸업생 1명이 단상 중앙에서 학장(가운 착용, 50대)에게 학위기 케이스를 두 손으로 받는 순간. 단상 왼쪽 아래 사회자 연단에 사회자 1명이 작은 카드를 들고 있다.
- 전경: 단상 아래 사진 구역에서 가족 3명(부모와 동생)이 스마트폰으로 촬영하며 웃고 있다. 어머니는 꽃다발을 들고 있다.
- 배경: 학위복 차림 졸업생 수십 명이 좌석에 앉아 박수, 뒤쪽 가족석에도 사람이 찬다. 다음 졸업생 2~3명이 단상 옆 계단 앞에 줄 서 있다.
- 금지: 이미지 안의 글자·현수막 문구·로고·학교 이름. 한글은 생성 모델이 깨뜨리므로 글자는 캡션으로만.
- 색조: 보라·회백 계열(제안서 강조색 #3B2A6B 와 어울리게), 과장 없는 다큐멘터리 사진 톤.

## English prompt (붙여 넣기용)

```
Documentary-style photograph of a small university graduation ceremony inside a Korean college auditorium (about 250 tiered seats), mid-afternoon in February. Soft winter daylight through side windows mixed with warm stage lighting.

Camera at the eye level of the front row of the family seating, 35mm lens, looking at the stage from about 30 degrees to the side, shallow depth of field focused on the stage.

On the low stage, one graduate in a black gown with a purple hood receives a diploma case with both hands from a dean in academic robes (Korean man or woman in their 50s); both are smiling. At the lower left of the stage, a master of ceremonies stands at a small lectern holding a plain index card. Two or three graduates in gowns wait in line at the side steps of the stage.

In the foreground, just below the stage, a Korean family of three (parents and a younger sibling) stands in a small open photo area, taking pictures with smartphones and laughing; the mother holds a bouquet of flowers. Behind them, rows of seated graduates in gowns applaud, and family members fill the back rows.

Natural skin tones, candid emotion, muted purple and warm grey color palette, realistic, high detail.

No text anywhere in the image: no banners, no signs, no logos, no letters, no writing on the diploma case or the lectern.
```

- 음수 프롬프트를 받는 모델(Midjourney `--no`, SD 계열)이면: `text, letters, banner, signage, logo, watermark, caption, distorted hands, extra fingers`
- 권장 비율: 16:9 (Midjourney `--ar 16:9`)

## 메모 (편집장에게)
- 결과물이 실제 행사 사진처럼 보이므로 제안서에 반드시 **"AI 생성 예시 이미지"** 로 표기할 것.
- 부산대 실제 건물·학위복 디자인을 재현한 것이 아니므로 캡션에 학교 고유 시설명을 붙이지 말 것.
