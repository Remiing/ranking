---
layout: default
title: 유니온 변화
nav_order: 3
---

# 유니온 변화
{: .fs-9 }

---

## 일간 유니온 변화

{{site.data.update_time[-2].update_time}} ~ {{site.data.update_time[-1].update_time}}
{: .text-right }

{% assign member_list = site.data.members %}
{% assign after_data = site.data.update_time[-1].filename | remove: ".csv" %}
{% assign after_data = site.data.chart[after_data] %}

{% assign before_data = site.data.update_time[-2].filename | remove: ".csv" %}
{% assign before_data = site.data.chart[before_data] %}

| 캐릭터 정보 | 이전 레벨 | 현재 레벨 | 레벨 변화 |
|:-|:-:|:-:|:-:|
{% for member in member_list -%}
  {%- assign before = before_data | where:"nickname", member[1] | first -%}
  {%- assign after = after_data | where:"nickname", member[1] | first -%}
  {%- unless before and after -%}{%- continue -%}{%- endunless -%}
  {%- assign before_union = before.union -%}
  {%- assign after_union = after.union -%}
  {%- assign union_change = after.union | minus: before.union -%}
  |{{after.nickname-}}
  |{{before.union-}}
  |{{after.union-}}
  |+{{union_change-}}|
{% endfor %}

---

## 주간 유니온 변화

{{site.data.update_time[-8].update_time}} ~ {{site.data.update_time[-1].update_time}}
{: .text-right }

{% assign before_data = site.data.update_time[-8].filename | remove: ".csv" %}
{% assign before_data = site.data.chart[before_data] %}

| 캐릭터 정보 | 이전 레벨 | 현재 레벨 | 레벨 변화 |
|:-|:-:|:-:|:-:|
{% for member in member_list -%}
  {%- assign before = before_data | where:"nickname", member[1] | first -%}
  {%- assign after = after_data | where:"nickname", member[1] | first -%}
  {%- unless before and after -%}{%- continue -%}{%- endunless -%}
  {%- assign before_union = before.union -%}
  {%- assign after_union = after.union -%}
  {%- assign union_change = after.union | minus: before.union -%}
  |{{after.nickname-}}
  |{{before.union-}}
  |{{after.union-}}
  |+{{union_change-}}|
{% endfor %}

