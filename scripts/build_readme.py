"""Rebuild the bilingual repository and per-video pages from data/videos.json."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1]
VIDEOS=json.loads((ROOT/'data/videos.json').read_text())
BANNER=json.loads((ROOT/'data/collection.json').read_text())['bannerUrl']
UTM='utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-motion-videos'
CTA='https://skillry.dev/skills?output=video&'+UTM
GROUPS=[('author_declared_claude_motion','Author-declared Claude Motion','作者声明的 Claude Motion 作品'),('mixed_workflow_claude_motion','Mixed workflows','混合工作流'),('recorded_generated_artifact','Recorded generated artifact','生成结果录屏'),('related_claude_motion_graphics_unconfirmed_claude_motion','Related motion references','其他动效参考')]
def esc(t):return html.escape(str(t),quote=True)
def anchor(t):return t.lower().replace(' ','-')
def card(v):
 preview=v['previewUrl'] if v['classification']=='author_declared_claude_motion' else v['posterUrl'].replace('https://media.skillry.dev/','https://media.skillry.dev/cdn-cgi/image/width=416,quality=80,fit=scale-down,format=auto/')
 handle=v['author_url'].split('/')[-1]
 return f'<td width="33%" valign="top"><a href="{v["videoUrl"]}"><img src="{preview}" alt="{esc(v["title"])}" width="100%"></a><br><b>{esc(v["title"])}</b><br><a href="{v["author_url"]}">@{esc(handle)}</a> · <a href="{v["videoUrl"]}">▶ Watch</a> · <a href="{v["post_url"]}">Original post</a> · <a href="cases/{v["id"]}.md">Details</a><br><sub>{round(v["durationSeconds"])}s · {esc(v["classificationLabel"])}</sub></td>'
def table(rows):
 return '<table>\n'+ '\n'.join('<tr>'+''.join(card(v) for v in rows[i:i+3])+'<td></td>'*(3-len(rows[i:i+3]))+'</tr>' for i in range(0,len(rows),3))+'\n</table>'
for zh in [False,True]:
 out=['# Awesome Claude Motion Videos','',('[English](README.md) · 简体中文' if zh else 'English · [简体中文](README.zh-CN.md)'),'',f'[![Videos](https://img.shields.io/badge/videos-{len(VIDEOS)}-121313)](data/videos.json) [![Author declared](https://img.shields.io/badge/author_declared-18-f4ff71?labelColor=121313)](#author-declared-claude-motion) [![Updated](https://img.shields.io/badge/updated-2026--10--12-2bb673)](data/changelog.json)','',f'<a href="{CTA}"><img src="{BANNER}" width="100%" alt="Community motion video collection"></a>','']
 if zh:
  out+=['来自 X 创作者的 **134 条完整视频**：品牌动效、产品介绍、科普、代码动画与视觉实验。每条保留作者主页、X 原帖、视频来源和识别依据；完整 MP4 与预览托管在 Cloudflare R2。','','**18 条作者明确声明使用 Claude Motion；4 条为混合工作流；1 条为生成结果录屏；111 条为相关动效参考，未确认使用 Claude Motion。** 作者声明属于来源证据，不等于独立验证制作过程，也不表示使用了某个同名产品。','','这些是作品案例；没有公开、明确逐字标注的提示词时，我们不会把作品描述包装成提示词。','',f'**[去 Skillry 找视频制作 Skills →]({CTA})** · 产品发布片、动效和讲解视频。','','## 视频目录','']
 else:
  out+=['**134 full-length community videos** collected from X: brand motion, product films, explainers, coded animation and visual experiments. Every entry credits its creator and links to the original post. MP4s and previews are hosted on Cloudflare R2.','','**18 author-declared Claude Motion works · 4 mixed workflows · 1 recorded generated artifact · 111 related motion references.** Related references are not confirmed Claude Motion works. Creator statements are attribution evidence, not independent verification of a production workflow or use of any particular product named Claude Motion.','','This is a collection of finished works. Descriptions are not presented as prompts when no clearly identified verbatim prompt is available.','',f'**[Find video-making Skills on Skillry →]({CTA})** · Launch films, motion graphics and explainers.','','## Contents','']
 for key,en,cn in GROUPS:
  group=[v for v in VIDEOS if v['classification']==key];out.append(f'- [{cn if zh else en}](#{anchor(en)}) ({len(group)})')
 out+=['- [Structured video index](data/videos.json)','- [Contributing](CONTRIBUTING.md)','- [Credits and media rights](MEDIA-RIGHTS.md)','']
 for key,en,cn in GROUPS:
  out +=[f'<a id="{anchor(en)}"></a>',f'## {cn if zh else en}','']
  if key.startswith('related_'):out+=[('以下为相关参考，不能据此认定使用了 Claude Motion。' if zh else 'These are related references, not confirmed Claude Motion works.'),'']
  out+=[table([v for v in VIDEOS if v['classification']==key]),'']
  if key=='author_declared_claude_motion':out+=[f'**[Explore video Skills on Skillry →]({CTA})**','']
 out+=[('## 继续创作' if zh else '## Make your own'),'']
 out+=[(f'在 [Skillry]({CTA}) 挑选适合产品发布片、动效或讲解视频的 Skill，把自己的文案和素材交给编程 Agent。参考创作者的思路，并遵守每位作者的作品权利。' if zh else f'Choose a video Skill on [Skillry]({CTA}), then give your coding agent your own brief and assets. Use the collection for inspiration and respect the creators\' rights.'),'',f'- [Linear Agent Style Launch Video](https://skillry.dev/skills/bs-linear-agent-style-launch-video?{UTM})',f'- [Notion Style Localize Video](https://skillry.dev/skills/bs-notion-style-localize-video?{UTM})','','Related collections: [Awesome Fable 5.5 Videos](https://github.com/yihui-dev/awesome-fable5-5-videos) · [Awesome Opus 5.5 Videos](https://github.com/yihui-dev/awesome-opus5-5-videos)','','## Credits','',('视频与相关第三方素材归各自权利人所有。仓库的 MIT 许可证仅覆盖我们编写的代码和原创文档，不授予视频、音乐或第三方品牌素材的使用权。修改或移除请求请提交 issue，并提供原帖和对应条目链接。' if zh else 'Videos and third-party assets belong to their respective rights holders. The MIT license covers our code and original documentation only; it does not license videos, music or third-party brand assets. Open an issue with the original post and entry link for corrections or removal requests.'),'']
 (ROOT/('README.zh-CN.md' if zh else 'README.md')).write_text('\n'.join(out))
(ROOT/'cases').mkdir(exist_ok=True)
for v in VIDEOS:
 lines=[f'# {v["title"]}','',f'By [{v["author_name"]}]({v["author_url"]}).','',f'[![{v["title"]}]({v["posterUrl"]})]({v["videoUrl"]})','',f'[▶ Full video]({v["videoUrl"]}) · [Original X post]({v["post_url"]}) · [Creator]({v["author_url"]})','',f'**Attribution:** {v["classificationLabel"]}',f'**Duration:** {v["durationSeconds"]} seconds','',f'**Recorded evidence (original language):** {v["evidence"]}','']
 if v.get('evidence_url'):lines+=[f'[Additional evidence]({v["evidence_url"]})','']
 if (v.get('source_detail_url') or '').startswith('https://'):lines+=[f'[Discovery source]({v["source_detail_url"]})','']
 lines+=['This entry is a finished-work reference, not a verified reproduction recipe. Refer to the creator\'s post for their own workflow and any prompt they chose to publish.','',f'[Find video-making Skills on Skillry →]({CTA})','','Media rights remain with their respective rights holders. See [MEDIA-RIGHTS.md](../MEDIA-RIGHTS.md).','']
 (ROOT/'cases'/f'{v["id"]}.md').write_text('\n'.join(lines))
print(f'Built bilingual README and {len(VIDEOS)} case pages.')
