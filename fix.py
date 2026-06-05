import re

filepath = r'e:\포폴\우산비서\usanbiseo\Usanbiseo\settings.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

mangled_css = """    /* 모달 스타일 */
    .modal-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      border: none;
      border-radius: 12px;
      font-size: 16px;
      font-weight: 700;
      margin-top: 10px;
      cursor: pointer;
      font-family: 'Manrope', sans-serif;
      transition: background 0.2s;
    }
    .save-btn:active {
      background: #4ab1d6;
    }"""

fixed_css = """    /* 저장하기 버튼 */
    .save-btn {
      width: 100%;
      height: 52px;
      background: #61c2e6;
      color: #ffffff;
      border: none;
      border-radius: 12px;
      font-size: 16px;
      font-weight: 700;
      margin-top: 10px;
      cursor: pointer;
      font-family: 'Manrope', sans-serif;
      transition: background 0.2s;
    }
    .save-btn:active {
      background: #4ab1d6;
    }

    /* 모달 스타일 */
    .modal-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.4);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 2000;
    }

    .modal-overlay.show {
      display: flex;
    }

    .modal-content {
      background: #fff;
      width: 85%;
      max-width: 320px;
      border-radius: 16px;
      padding: 32px 24px 24px;
      position: relative;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
      animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    @keyframes popIn {
      0% { transform: scale(0.8); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }

    .modal-content .close-btn {
      position: absolute;
      top: 14px;
      right: 14px;
      background: none;
      border: none;
      cursor: pointer;
    }

    .modal-content .close-btn svg {
      width: 22px;
      height: 22px;
      stroke: #a0a0a0;
      stroke-width: 2;
      fill: none;
    }"""

content = content.replace(mangled_css, fixed_css)

html_mangled = """        </div>
        </div>
      </section>

      <button class="save-btn\""""

html_fixed = """        </div>
      </section>

      <button class="save-btn\""""

content = content.replace(html_mangled, html_fixed)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
