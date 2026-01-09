#!/usr/bin/env python3
"""
API Misery Index - Because third-party APIs are like exes: unpredictable and full of surprises.
"""

import json
import difflib
from datetime import datetime
from typing import Dict, Any, Optional

class APIMiseryIndex:
    """
    Measures how much pain an API is causing you.
    Higher score = more tears in your coffee.
    """
    
    def __init__(self, api_name: str = "Unknown API"):
        self.api_name = api_name
        self.responses = []  # Like a therapist's notes, but for APIs
        self.errors = []     # The graveyard of broken dreams
        
    def log_response(self, response_data: Dict[str, Any]) -> None:
        """Log a response. Warning: may cause existential dread."""
        self.responses.append({
            'timestamp': datetime.now().isoformat(),
            'data': response_data
        })
        
    def log_error(self, error_msg: str) -> None:
        """Log an error. Comes with free emotional baggage."""
        self.errors.append({
            'timestamp': datetime.now().isoformat(),
            'message': error_msg
        })
    
    def calculate_misery(self) -> float:
        """
        Calculate misery score (0-100).
        0 = "It just works" (mythical)
        100 = "Why did I choose this career?"
        """
        if not self.responses:
            return 0.0  # No data, no misery (yet)
            
        misery = 0.0
        
        # 1. Inconsistency penalty (40%)
        if len(self.responses) > 1:
            last_two = [json.dumps(r['data'], sort_keys=True) 
                       for r in self.responses[-2:]]
            if last_two[0] != last_two[1]:
                misery += 40  # API changed its mind. Again.
        
        # 2. Error penalty (30%)
        misery += min(30, len(self.errors) * 10)
        
        # 3. Schema complexity penalty (30%)
        if self.responses:
            sample = json.dumps(self.responses[-1]['data'])
            # More nesting = more pain
            nesting = sample.count('{') + sample.count('[')
            misery += min(30, nesting * 2)
        
        return min(100.0, misery)
    
    def get_diagnosis(self) -> str:
        """Returns a helpful (snarky) diagnosis."""
        score = self.calculate_misery()
        
        if score < 20:
            return f"{self.api_name}: Suspiciously stable. Check if it's actually running."
        elif score < 50:
            return f"{self.api_name}: Mild annoyance. You'll only cry a little."
        elif score < 80:
            return f"{self.api_name}: Significant suffering. Time for a strong drink."
        else:
            return f"{self.api_name}: CRITICAL. Abandon all hope ye who integrate here."

# Example usage (because documentation is for quitters)
if __name__ == "__main__":
    misery = APIMiseryIndex("ExampleAPI")
    
    # Simulate some API pain
    misery.log_response({"status": "ok", "data": {"id": 1}})
    misery.log_response({"status": "success", "result": {"user_id": 1}})  # Oops, changed!
    misery.log_error("404: Endpoint moved to /v2 (but we're on v3)")
    
    print(f"Misery Score: {misery.calculate_misery():.1f}")
    print(f"Diagnosis: {misery.get_diagnosis()}")
