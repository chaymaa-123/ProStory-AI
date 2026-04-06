'use client'

import { useState } from 'react'
import { Badge } from '@/components/ui/badge'
import { X } from 'lucide-react'

interface TagInputProps {
  value: string[]
  onChange: (tags: string[]) => void
  placeholder?: string
  maxTags?: number
  suggestedTags?: string[]
}

export function TagInput({
  value,
  onChange,
  placeholder = 'Add tags (press Enter to add)',
  maxTags = 10,
  suggestedTags = [
    'Remote Work',
    'Career Growth',
    'Company Culture',
    'Team Leadership',
    'Work-Life Balance',
    'Innovation',
    'Collaboration',
    'Professional Development',
  ],
}: TagInputProps) {
  const [input, setInput] = useState('')
  const [filteredSuggestions, setFilteredSuggestions] = useState<string[]>([])

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value
    setInput(val)

    if (val.trim()) {
      const filtered = suggestedTags.filter(
        (tag) =>
          tag.toLowerCase().includes(val.toLowerCase()) &&
          !value.includes(tag)
      )
      setFilteredSuggestions(filtered)
    } else {
      setFilteredSuggestions([])
    }
  }

  const handleAddTag = (tag: string) => {
    const trimmedTag = tag.trim()
    if (
      trimmedTag &&
      !value.includes(trimmedTag) &&
      value.length < maxTags
    ) {
      onChange([...value, trimmedTag])
      setInput('')
      setFilteredSuggestions([])
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault()
      handleAddTag(input)
    }
  }

  const handleRemoveTag = (tag: string) => {
    onChange(value.filter((t) => t !== tag))
  }

  return (
    <div className="space-y-3">
      <div className="relative">
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          className="w-full px-4 py-2 border border-border rounded-lg bg-background text-foreground placeholder-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
        />

        {/* Suggestions dropdown */}
        {filteredSuggestions.length > 0 && (
          <div className="absolute top-full mt-1 w-full bg-background border border-border rounded-lg shadow-lg z-10">
            {filteredSuggestions.map((tag) => (
              <button
                key={tag}
                onClick={() => handleAddTag(tag)}
                className="w-full text-left px-4 py-2 hover:bg-muted text-sm text-foreground transition-colors first:rounded-t-lg last:rounded-b-lg"
              >
                {tag}
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Tags display */}
      {value.length > 0 && (
        <div className="flex gap-2 flex-wrap">
          {value.map((tag) => (
            <Badge key={tag} variant="secondary" className="pr-1">
              {tag}
              <button
                onClick={() => handleRemoveTag(tag)}
                className="ml-2 hover:bg-black/20 rounded-full p-0 w-4 h-4 flex items-center justify-center"
              >
                <X className="w-3 h-3" />
              </button>
            </Badge>
          ))}
        </div>
      )}

      {/* Tag count */}
      <div className="text-xs text-muted-foreground">
        {value.length} / {maxTags} tags
      </div>
    </div>
  )
}
