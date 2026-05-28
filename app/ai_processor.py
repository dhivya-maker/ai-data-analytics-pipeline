import json
from openai import OpenAI
client  = OpenAI()
def process_text_with_ai(text):
    prompt = f"""
        Analyze the following customer support text.

        Return ONLY valid JSON with:
        - summary
        - category
        - issue_type
        - priority
        - sentiment

        Text:
        {text}
        """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    result = response.output_text

    # response from openai ```json
    # {
    #   "summary": "Customer reported delayed claim processing due to missing provider information; issue has been escalated to the claims team.",
    #   "category": "Claims",
    #   "issue_type": "Delayed Processing",
    #   "priority": "High",
    #   "sentiment": "Negative"
    # }
    # ```

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()
    try:
        return json.loads(result)

    except json.JSONDecodeError:
        print("\nJSON parsing failed.")

        return {
            "summary": "Parsing Error",
            "category": "Unknown",
            "issue_type": "Unknown",
            "priority": "Unknown",
            "sentiment": "Unknown",
            "recommended_action": "Check AI response formatting."
        }