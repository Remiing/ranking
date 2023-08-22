---
layout: default
title: 유니온 변화
nav_order: 3
---

# 유니온 변화
{: .fs-9 }

---

{% assign member_list = site.data.members %}
{% assign after_data = site.data.update_time[-1].filename | remove: ".csv" %}
{% assign after_data = site.data.chart[after_data] %}


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

---

{% assign union_increase = site.data.union_increase %}
{%- for row in union_increase -%}
  {%- capture date %}{{date}}"{{row[nil] | date: "%m/%d"}}",{% endcapture -%}
  {%- capture chr0 %}{{chr0}}{{row["박종우123"]}},{% endcapture -%}
  {%- capture chr1 %}{{chr1}}{{row["도적삼식"]}},{% endcapture -%}
  {%- capture chr2 %}{{chr2}}{{row["핫다주"]}},{% endcapture -%}
  {%- capture chr3 %}{{chr3}}{{row["DEX중독"]}},{% endcapture -%}
  {%- capture chr4 %}{{chr4}}{{row["으뜸기사"]}},{% endcapture -%}
  {%- capture chr5 %}{{chr5}}{{row["뜨겁초"]}},{% endcapture -%}
{% endfor %}


<canvas id="union" style="box-sizing: border-box; width: 100%;"></canvas>


<script>
var options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      }, 
    },
    layout: {
      padding: {
        top: 32,
        right: 32,
        bottom: 16,
        left: 8
      }
    },
    aspectRatio: 1,
};

var ctx = document.getElementById("union");

var labels = [{{date}}];
var data = {
    labels: labels,
    datasets: [
      {
        label: "박종우123",
        data: [{{chr0}}],
        backgroundColor: "rgba(33, 160, 221, 0.5)",
        borderColor: "rgba(33, 160, 221, 1)",
      },
      {
        label: "도적삼식",
        data: [{{chr1}}],
        backgroundColor: "rgba(45, 40, 40, 0.5)",
        borderColor: "rgba(45, 40, 40, 1)",
      },
      {
        label: "핫다주",
        data: [{{chr2}}],
        backgroundColor: "rgba(243, 228, 50, 0.5)",
        borderColor: "rgba(243, 228, 50, 1)",
      },
      {
        label: "DEX중독",
        data: [{{chr3}}],
        backgroundColor: "rgba(186, 110, 182, 0.5)",
        borderColor: "rgba(186, 110, 182, 1)",
      },
      {
        label: "으뜸기사",
        data: [{{chr4}}],
        backgroundColor: "rgba(250, 225, 134, 0.5)",
        borderColor: "rgba(250, 225, 134, 1)",
      },
      {
        label: "뜨겁초",
        data: [{{chr5}}],
        backgroundColor: "rgba(225, 104, 136, 0.5)",
        borderColor: "rgba(225, 104, 136, 1)",
      },
    ]
  };

new Chart(ctx, {
  type: "line",
  data: data, 
  options: options, 
});
</script>
