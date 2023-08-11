---
layout: default
title: 레벨 변화
nav_order: 2
---

# 레벨 변화
{: .fs-9 }

---

## 일간 레벨 변화

{{site.data.update_time[-2].update_time}} ~ {{site.data.update_time[-1].update_time}}
{: .text-right }

{% assign member_list = site.data.members %}
{% assign after_data = site.data.update_time[-1].filename | remove: ".csv" %}
{% assign after_data = site.data.chart[after_data] %}

{% assign before_data = site.data.update_time[-2].filename | remove: ".csv" %}
{% assign before_data = site.data.chart[before_data] %}

| 캐릭터 정보 | 이전 레벨 | 현재 레벨 | 레벨 변화 | 경험치 변화 |
|:-|:-:|:-:|:-:|:-:|
{% for member in member_list -%}
  {%- assign before = before_data | where:"nickname", member[1] | first -%}
  {%- assign after = after_data | where:"nickname", member[1] | first -%}
  {%- unless before and after -%}{%- continue -%}{%- endunless -%}
  {%- assign before_level = before.level -%}
  {%- assign after_level = after.level -%}
  {%- assign before_exp = before.experience -%}
  {%- assign after_exp = after.experience -%}
  {%- assign level_change = after.level | minus: before.level -%}
  {%- assign start = before_level -%}
  {%- assign end = after_level | minus: 1 -%}
  {%- assign exp_change = 0 -%}
  {%- for level_step in (start..end) -%}
    {%- assign exp_change = exp_change | plus: site.data.experience[level_step] -%}
  {%- endfor -%}
  {%- assign exp_change = exp_change | plus: after_exp -%}
  {%- assign exp_change = exp_change | minus: before_exp -%}
  |{{after.nickname-}}
  |{{before.level-}}
  |{{after.level-}}
  |+{{level_change-}}
  |{{exp_change | divided_by: 100000000 }}억|
{% endfor %}

---

## 주간 레벨 변화

{{site.data.update_time[-8].update_time}} ~ {{site.data.update_time[-1].update_time}}
{: .text-right }

{% assign before_data = site.data.update_time[-8].filename | remove: ".csv" %}
{% assign before_data = site.data.chart[before_data] %}

| 캐릭터 정보 | 이전 레벨 | 현재 레벨 | 레벨 변화 | 경험치 변화 |
|:-|:-:|:-:|:-:|:-:|
{% for member in member_list -%}
  {%- assign before = before_data | where:"nickname", member[1] | first -%}
  {%- assign after = after_data | where:"nickname", member[1] | first -%}
  {%- unless before and after -%}{%- continue -%}{%- endunless -%}
  {%- assign before_level = before.level -%}
  {%- assign after_level = after.level -%}
  {%- assign before_exp = before.experience -%}
  {%- assign after_exp = after.experience -%}
  {%- assign level_change = after.level | minus: before.level -%}
  {%- assign start = before_level -%}
  {%- assign end = after_level | minus: 1 -%}
  {%- assign exp_change = 0 -%}
  {%- for level_step in (start..end) -%}
    {%- assign exp_change = exp_change | plus: site.data.experience[level_step] -%}
  {%- endfor -%}
  {%- assign exp_change = exp_change | plus: after_exp -%}
  {%- assign exp_change = exp_change | minus: before_exp -%}
  |{{after.nickname-}}
  |{{before.level-}}
  |{{after.level-}}
  |+{{level_change-}}
  |{{exp_change | divided_by: 100000000 }}억|
{% endfor %}

