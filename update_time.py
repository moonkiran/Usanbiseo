# update_time.py
import re

hours = '\n'.join([f'<option value="{h:02d}"{" selected" if h==8 else ""}>{h:02d}</option>' for h in range(24)])
hours_in = '\n'.join([f'<option value="{h:02d}"{" selected" if h==18 else ""}>{h:02d}</option>' for h in range(24)])
mins = '\n'.join([f'<option value="{m:02d}"{" selected" if m==30 else ""}>{m:02d}</option>' for m in range(0, 60, 5)])

html = f'''        <div class="time-cards">
          <div class="time-card">
            <span class="label">외출 시간</span>
            <div class="time-value">
              <div class="time-part">
                <span id="out-hour">08</span>
                <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <select onchange="document.getElementById('out-hour').innerText = this.value">
{hours}
                </select>
              </div>
              <span class="colon">:</span>
              <div class="time-part">
                <span id="out-minute">30</span>
                <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <select onchange="document.getElementById('out-minute').innerText = this.value">
{mins}
                </select>
              </div>
            </div>
          </div>
          <div class="time-card">
            <span class="label">귀가 시간</span>
            <div class="time-value">
              <div class="time-part">
                <span id="in-hour">18</span>
                <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <select onchange="document.getElementById('in-hour').innerText = this.value">
{hours_in}
                </select>
              </div>
              <span class="colon">:</span>
              <div class="time-part">
                <span id="in-minute">30</span>
                <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <select onchange="document.getElementById('in-minute').innerText = this.value">
{mins}
                </select>
              </div>
            </div>
          </div>
        </div>'''

with open('e:/포폴/우산비서/usanbiseo/Usanbiseo/settings.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="time-cards">.*?</div>\s*</section>', html + '\n      </section>', content, flags=re.DOTALL)

with open('e:/포폴/우산비서/usanbiseo/Usanbiseo/settings.html', 'w', encoding='utf-8') as f:
    f.write(content)
