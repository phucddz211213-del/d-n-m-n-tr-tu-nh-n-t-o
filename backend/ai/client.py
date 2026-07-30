import os
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

class AIClient:
    def redact_for_logging(self, summary):
        # only keep totals by category
        return {"month": summary.get("month"), "categories": [{"name": c.get("name"), "total": float(c.get("total", 0))} for c in summary.get("categories", [])]}

    def build_monthly_report_prompt(self, summary):
        lines = "\n".join([f"- {c['name']}: {c['total']}" for c in summary.get("categories", [])])
        prompt = (
            "System: Bạn là trợ lý chi tiêu cá nhân. Chỉ đưa gợi ý tham khảo, không tư vấn tài chính chuyên nghiệp.\n"
            f"User: Dữ liệu chi tiêu tháng {summary.get('month')}:\n{lines}\n"
            "Hãy tóm tắt xu hướng trong 5 câu, liệt kê 3 khoản cần điều chỉnh và gợi ý ngân sách cho 3 danh mục tốn nhiều nhất. Trả lời ngắn gọn, tiếng Việt."
        )
        return prompt

    def call(self, prompt):
        if not OPENAI_API_KEY:
            return "(AI engine not configured)"
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": OPENAI_MODEL,
            "messages": [{"role":"system","content":"You are an assistant."},{"role":"user","content":prompt}],
            "max_tokens": 400
        }
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()
        choices = data.get("choices") or []
        if not choices:
            return ""
        return choices[0].get("message", {}).get("content", "")
