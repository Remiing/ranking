---
layout: default
title: Ranking
nav_order: 1
description: ""
permalink: /
---

# Ranking
{: .fs-9 }

에악회 랭킹
{: .fs-6 .fw-300 }

---

매일 새벽 5~6시에 갱신됩니다. <br>
Last Update {{site.data.update_time[-1].update_time}}
{: .text-right }

{% assign last_data = site.data.update_time[-1].filename | remove: ".csv" %}
{% assign members_data = site.data.chart[last_data] %}

| 순위 | 스트리머 |  | 캐릭터 정보 | 레벨 | 유니온 | 인기도 |
|:-:|:-|:-:|:-|:-:|:-:|:-:|
{% assign rank = 1 -%}
{% for member in members_data -%}
|{{rank}}{%- assign rank = rank | plus: 1 -%}
|{{member.streamer-}}
|<span>![](./assets/images/character/{{member.nickname}}.png){: .character-img}</span>{{-raw-}}
|{{member.nickname-}}<br>{{member.class-}}
|{{member.level-}}
|{{member.union-}}
|{{member.popularity-}}|
{% endfor %}




